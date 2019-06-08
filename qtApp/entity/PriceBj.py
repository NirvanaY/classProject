#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
import time
from qtApp import db


class PriceBj(db.Model):

    # 表名设置
    __tablename__ = 'tbl_price_beijing'

    # 项目编号
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 项目的创建时间
    ctime = db.Column(db.DateTime, nullable=True)
    # 所在机房
    availability_zone = db.Column(db.String(255), nullable=False)
    # 实例类型
    instance_type_as_string = db.Column(db.String(255), nullable=False)
    # 操作系统
    product_description_as_string = db.Column(db.String(255), nullable=False)
    # 拐点价格
    spot_price = db.Column(db.DECIMAL(12, 6), nullable=False)
    # 拐点时间
    change_time = db.Column(db.BIGINT, nullable=False)

    def __init__(self, availability_zone, instance_type_as_string,
                 product_description_as_string, spot_price, change_time, ctime=time.localtime()):

        self.ctime = ctime
        self.availability_zone = availability_zone
        self.instance_type_as_string = instance_type_as_string
        self.product_description_as_string = product_description_as_string
        self.spot_price = spot_price
        self.change_time = change_time

    def __repr__(self):

        return '< PriceBj availability_zone: {}, ' \
               'instance_type_as_string: {}, ' \
               'product_description_as_string: {}, ' \
               'spot_price: {}, ' \
               'change_time: {}, ' \
               'ctime: {} >'.format(self.availability_zone,
                                    self.instance_type_as_string,
                                    self.product_description_as_string,
                                    self.spot_price,
                                    self.change_time,
                                    self.ctime)


if __name__ == '__main__':
    pass
