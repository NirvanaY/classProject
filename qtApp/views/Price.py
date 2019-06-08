#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
import time
import json
import requests
from flask import current_app
from qtApp.params.AWSPriceRequest import GetPriceRequiredParams, GetPriceNotNecessaryParams
from qtApp.constant.ParamsName import PriceRecordReadParams
from qtApp.result import CodeMsg
from qtApp.utils import DateUtil
from qtApp.utils.OSUtil import OSUtil
from qtApp.constant.AWSProperties import Region
from qtApp.entity.PriceBj import PriceBj
from qtApp.entity.PriceNx import PriceNx
from qtApp.entity.RecordCSV import RecordCSV
from qtApp.database.DBOperation import DBOperation
from qtApp.database.PriceOperation import DBPrice
from qtApp.database.SystemDictOperation import SysDict


def get_price_by_time(start_time: int, end_time: int, region: str):

    ''' 解析历史数据入库

    :param start_time: 指定开始时间
    :param end_time: 指定结束时间
    :param region: 指定地区
    :return:
    '''

    # 请求地址
    request_url = current_app.config['AWS_REQUEST_ADDRESS']

    # 可选参数设置：开始时间和结束时间
    time_params = GetPriceNotNecessaryParams(start_time=start_time, end_time=end_time)
    # 必选参数设置：指定大区范围
    history_price_params = GetPriceRequiredParams(time_params, region)
    # 参数转json
    request_params = json.dumps(history_price_params, default=lambda obj: obj.__dict__)

    # 发送请求获取历史定价记录
    aws_spot_history_price_result = requests.post(request_url, data=request_params).json()

    # 数据读取成功
    if aws_spot_history_price_result[PriceRecordReadParams.code] == CodeMsg.SUCCEES.code:

        # 读取数据信息
        price_record_list = aws_spot_history_price_result[PriceRecordReadParams.data]
        # 解析数据入库
        read_price_records_list(region, price_record_list)
    else:
        pass


def read_price_records_list(region: str, price_record_list: list):

    ''' 读取价格记录添加到数据库

    :param region: 地区
    :param price_record_list: 价格记录
    :return:
    '''

    records = []

    for price_record in price_record_list:

        # 将格林威治时间转化为时间戳
        date_time = DateUtil.format_greenwich(price_record[PriceRecordReadParams.timestamp])

        if region.__eq__(Region.Beijing):

            record = beijing_entity(price_record, date_time)

            # 查询数据库是否有该记录信息
            db_record = DBPrice.find_bj(availability_zone=record.availability_zone,
                                        instance_type_as_string=record.instance_type_as_string,
                                        product_description_as_string=record.product_description_as_string,
                                        spot_price=record.spot_price,
                                        record_time=date_time)

        elif region.__eq__(Region.NingXia):

            record = ningxia_entity(price_record, date_time)

            # 查询数据库是否有该记录信息
            db_record = DBPrice.find_nx(availability_zone=record.availability_zone,
                                        instance_type_as_string=record.instance_type_as_string,
                                        product_description_as_string=record.product_description_as_string,
                                        spot_price=record.spot_price,
                                        record_time=date_time)

        # 数据库已存在该记录则不执行插入操作
        if len(db_record) == 0:
            records.append(record)

    DBOperation.add_all(records)


def beijing_entity(price_record, record_time):

    ''' 北京记录

    :param price_record: 价格记录
    :param record_time: 时间戳
    :return:
    '''

    record = PriceBj(availability_zone=price_record[PriceRecordReadParams.availabilityZone],
                     instance_type_as_string=price_record[PriceRecordReadParams.instanceTypeAsString],
                     product_description_as_string=price_record[PriceRecordReadParams.productDescriptionAsString],
                     spot_price=price_record[PriceRecordReadParams.spotPrice],
                     change_time=record_time)
    return record


def ningxia_entity(price_record, record_time):

    ''' 北京记录

    :param price_record: 价格记录
    :param record_time: 时间戳
    :return:
    '''

    record = PriceNx(availability_zone=price_record[PriceRecordReadParams.availabilityZone],
                     instance_type_as_string=price_record[PriceRecordReadParams.instanceTypeAsString],
                     product_description_as_string=price_record[PriceRecordReadParams.productDescriptionAsString],
                     spot_price=price_record[PriceRecordReadParams.spotPrice],
                     change_time=record_time)
    return record


def create_csv_records():

    ''' 生成csv文件供训练模型

    :return:
    '''

    # 获取查询条件
    zones, types, oss = get_select_condition()

    for zone in zones:
        for ins in types:
            for os_type in oss:
                # 生成csv文件供训练模型
                create_csv(zone, ins, os_type)


def create_path():

    ''' 生成保存csv文件的文件夹

    :return:
    '''

    path = './csv_data/{date}/'
    path = path.format(date=time.strftime("%Y-%m-%d", time.localtime()))
    OSUtil.mkdir(path)

    return path


def get_select_condition():

    ''' 获取数据记录

    :return:
    '''

    zone_list = SysDict.find_by_column_type('availability_zone')
    type_list = SysDict.find_by_column_type('instance_type_as_string')
    os_list = SysDict.find_by_column_type('product_description_as_string')

    return zone_list, type_list, os_list


def create_csv(zone, ins, os_type):

    '''生成csv文件

    :param zone: 区域
    :param ins: 实例
    :param os_type: 操作系统
    :return:
    '''

    # 获取记录
    records = find_records(zone, ins, os_type)
    # 没有记录终止操作
    if len(records) == 0:
        return

    # 获取文件保存路径
    path = create_path()
    # 生成文件名
    file_name = '{zone}{os}-{ins}.csv'.format(zone=zone.labels, os=os_type.labels, ins=str(ins.values_num))

    # csv_row模板信息
    csv_row = '{row},{price},{time}\n'

    # 将记录写入csv文件
    with open(path + file_name, 'w') as f:
        for i in range(len(records)):
            f.write(csv_row.format(row=str(i+1), price=str(records[i].spot_price), time=records[i].change_time))

    # 将csv生成记录写入数据库
    csv = RecordCSV(date_folder=time.strftime("%Y-%m-%d", time.localtime()),
                    file_path=path, file_name=file_name, path_name=path + file_name)
    DBOperation.add(csv)


def find_records(zone, ins, os_type):

    ''' 根据条件从数据库中获取指定记录

    :param zone: 地区
    :param ins: 实例
    :param os_type: 操作系统
    :return:
    '''
    if zone.value_type.startswith('cn-northwest'):

        records = DBPrice.nx_by_zone_type_os(availability_zone=zone.value_type,
                                             instance_type_as_string=ins.value_type,
                                             product_description_as_string=os_type.value_type)
    elif zone.value_type.startswith('cn-north'):

        records = DBPrice.bj_by_zone_type_os(availability_zone=zone.value_type,
                                             instance_type_as_string=ins.value_type,
                                             product_description_as_string=os_type.value_type)

    return records


if __name__ == '__main__':
    pass
