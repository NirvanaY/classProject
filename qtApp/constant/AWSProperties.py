#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com


class Method(object):

    ''' aws提供的获取历史定价的参数

    该方法是固定值

    参数:
        historyPrice: 获取历史报价
    '''

    # 获取历史报价
    historyPrice = 'aws.ec2.spotInstanceRequest.priceHistory'


class AwsKey(object):

    ''' aws认证信息

    调用aws接口的认证信息

    参数:
        cloudAccessKey: 链接AWS的key值信息
        cloudSecretKey: 链接AWS的key值信息
    '''

    # 链接AWS的key值信息：cloudAccessKey
    cloudAccessKey = 'AKIAOIR6XRU5JNRV6TJA'
    # 链接AWS的key值信息：cloudSecretKey
    cloudSecretKey = 'ZDTv73W9W3ONI59Tmii1TOVTPmkkRk/PMppS0i1e'


class Region(object):

    ''' aws中国地区大区划分

    中国区大区划分，暂时只有北京区和宁夏区

    参数:
        Beijing: 北京区
        NingXia: 宁夏区
    '''

    # 北京区
    Beijing = 'cn-north-1'
    # 宁夏区
    NingXia = 'cn-northwest-1'

    cloudRegion = [Beijing, NingXia]


if __name__ == '__main__':
    pass
