#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com


class PriceRecordReadParams(object):

    ''' 历史定价记录中的参数名

    调用agent提供的方法获取历史定价，记录中包含以下字段信息

    参数:
        data: 返回结果集中的总数据
        availabilityZone: 机房信息
        instanceTypeAsString: 实例类型
        productDescriptionAsString: 实例机型{Windows, Linux/UNIX}
        spotPrice: 定价
        timestamp: 价格拐点时间
    '''

    # 状态码：用来判断是否请求到数据
    code = 'code'

    # 返回结果集中的总数据
    data = 'data'

    # 机房信息
    availabilityZone = 'availabilityZone'
    # 实例类型
    instanceTypeAsString = 'instanceTypeAsString'
    # 实例机型{Windows, Linux/UNIX}
    productDescriptionAsString = 'productDescriptionAsString'
    # 定价
    spotPrice = 'spotPrice'
    # 价格拐点时间
    timestamp = 'timestamp'


class TimeFormatString(object):

    ''' 格式化时间转换字符串

    参数:
        GREENWICH: 格林威治世界时格式
        YYYY_MM_DD: 年月日
    '''

    GREENWICH = '%Y-%m-%dT%H:%M:%SZ'

    YYYY_MM_DD = '%Y-%m-%d'


if __name__ == '__main__':
    pass
