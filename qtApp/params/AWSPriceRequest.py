#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
from qtApp.constant.AWSProperties import Method, AwsKey


class GetPriceRequiredParams(object):

    '''
        获取价格信息的必须参数类
    '''

    def __init__(self, params, region, method=Method.historyPrice,
                 cloud_access_key=AwsKey.cloudAccessKey, cloud_secret_key=AwsKey.cloudSecretKey):

        # aws获取历史价格的方法
        self.method = method
        # 可选参数: 实例类型、开始时间、结束时间、机房选择
        self.params = params
        # aws访问信息：cloudAccessKey
        self.cloudAccessKey = cloud_access_key
        # aws访问信息：cloudSecretKey
        self.cloudSecretKey = cloud_secret_key
        # 地区信息
        self.cloudRegion = region

    def __repr__(self):

        return '< method: {}, params: {}, cloud_access_key: {}, ' \
               'cloudSecretKey: {}, region: {} >'.format(self.method,
                                                         self.params,
                                                         self.cloudAccessKey,
                                                         self.cloudSecretKey,
                                                         self.cloudRegion)


class GetPriceNotNecessaryParams(object):

    '''
        获取价格信息非必须参数类
        通过非必须参数的指定可以获取指定类型、时间、机房的实例信息
    '''

    def __init__(self, instance_types=None, start_time=None,
                 end_time=None, availability_zones=None, product_descriptions=None):

        # 实例类型
        self.instanceTypes = instance_types
        # 开始时间
        self.startTime = start_time
        # 结束时间
        self.endTime = end_time
        # 机房信息
        self.availabilityZones = availability_zones
        # 实例操作系统
        self.productDescriptions = product_descriptions

    def __repr__(self):

        return '< instanceTypes: {}, startTime: {}, endTime: {}, availabilityZone: {}, productDescriptions: {} >'\
            .format(self.instanceTypes, self.startTime, self.endTime, self.availabilityZones, self.productDescriptions)


if __name__ == '__main__':
    pass
