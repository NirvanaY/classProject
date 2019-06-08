#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
import time
from qtApp import db


class SystemDict(db.Model):

    # 表名设置
    __tablename__ = 'tbl_system_dict'

    # 项目编号
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建时间
    ctime = db.Column(db.DateTime, nullable=True)
    # 更新时间
    utime = db.Column(db.DateTime, nullable=True)
    # 对应字段
    column_type = db.Column(db.String(255), nullable=False)
    # 该字段下所有的value值
    value_type = db.Column(db.String(255), nullable=False)
    # value值对应的数值
    values_num = db.Column(db.Integer, nullable=False)
    # 标签
    labels = db.Column(db.String(255), nullable=False)
    # 排序
    sort = db.Column(db.Integer, nullable=False)
    # 备注
    remarks = db.Column(db.String(255), nullable=True)
    # 删除标记：只做逻辑删除，不做屋里删除---》0:删除，1:存在
    del_flag = db.Column(db.Integer, default=1, nullable=False)

    def __init__(self, column_type, value_type, values_num, labels, sort, remarks,
                 ctime=time.localtime(), utime=time.localtime(), del_flag=1):

        self.ctime = ctime
        self.utime = utime
        self.column_type = column_type
        self.value_type = value_type
        self.values_num = values_num
        self.labels = labels
        self.sort = sort
        self.remarks = remarks
        self.del_flag = del_flag

    def __repr__(self):

        return '< SystemDict id: {}, ' \
               'ctime: {}, ' \
               'utime: {}, ' \
               'column_type: {}, ' \
               'value_type: {}, ' \
               'values_num: {}, ' \
               'labels: {}, ' \
               'sort: {}, ' \
               'remarks: {}, ' \
               'del_flag: {} >'.format(self.id, self.ctime, self.utime, self.column_type, self.value_type,
                                       self.values_num, self.labels, self.sort, self.remarks, self.del_flag)


if __name__ == '__main__':
    pass
