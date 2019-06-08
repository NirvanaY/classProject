#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
from qtApp.database.DBOperation import DBOperation
from qtApp.entity.PriceBj import PriceBj
from qtApp.entity.PriceNx import PriceNx


class DBPrice(DBOperation):

    @staticmethod
    def find_bj(availability_zone, instance_type_as_string, product_description_as_string, spot_price, record_time):

        ''' 查找北京区价格记录

        :param availability_zone: 机房
        :param instance_type_as_string: 实例类型
        :param product_description_as_string: 操作系统
        :param spot_price: 价格
        :param record_time: 时间
        :return:
        '''

        return PriceBj.query.filter_by(availability_zone=availability_zone,
                                       instance_type_as_string=instance_type_as_string,
                                       product_description_as_string=product_description_as_string,
                                       spot_price=spot_price,
                                       change_time=record_time).all()

    @staticmethod
    def find_nx(availability_zone, instance_type_as_string, product_description_as_string, spot_price, record_time):

        ''' 查找宁夏区价格记录

        :param availability_zone: 机房
        :param instance_type_as_string: 实例类型
        :param product_description_as_string: 操作系统
        :param spot_price: 价格
        :param record_time: 时间
        :return:
        '''

        return PriceNx.query.filter_by(availability_zone=availability_zone,
                                       instance_type_as_string=instance_type_as_string,
                                       product_description_as_string=product_description_as_string,
                                       spot_price=spot_price,
                                       change_time=record_time).all()

    @staticmethod
    def bj_by_zone_type_os(availability_zone, instance_type_as_string, product_description_as_string):

        ''' 查找北京区价格记录

        :param availability_zone: 机房
        :param instance_type_as_string: 实例类型
        :param product_description_as_string: 操作系统
        :return:
        '''

        return PriceBj.query.filter_by(availability_zone=availability_zone,
                                       instance_type_as_string=instance_type_as_string,
                                       product_description_as_string=product_description_as_string)\
            .order_by(PriceBj.change_time.asc()).all()

    @staticmethod
    def nx_by_zone_type_os(availability_zone, instance_type_as_string, product_description_as_string):

        ''' 查找宁夏区价格记录

        :param availability_zone: 机房
        :param instance_type_as_string: 实例类型
        :param product_description_as_string: 操作系统
        :return:
        '''

        return PriceNx.query.filter_by(availability_zone=availability_zone,
                                       instance_type_as_string=instance_type_as_string,
                                       product_description_as_string=product_description_as_string)\
            .order_by(PriceNx.change_time.asc()).all()


if __name__ == '__main__':
    pass
