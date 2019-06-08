#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
import time
from qtApp import db


class RecordCSV(db.Model):

    # 表名设置
    __tablename__ = 'tbl_records_csv'

    # 项目编号
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 文件夹
    date_folder = db.Column(db.String(10), nullable=False)
    # 文件路径
    file_path = db.Column(db.String(255), nullable=False)
    # 文件名
    file_name = db.Column(db.String(255), nullable=False)
    # 地址
    path_name = db.Column(db.String(255), nullable=False)
    # 创建时间
    ctime = db.Column(db.DateTime, nullable=False)

    def __init__(self, date_folder, file_path, file_name, path_name, ctime=time.localtime()):
        self.date_folder = date_folder
        self.file_path = file_path
        self.file_name = file_name
        self.path_name = path_name
        self.ctime = ctime

    def __repr__(self):
        return '< RecordCSV id: {}, ' \
               'date_folder: {}, ' \
               'file_path: {}, ' \
               'file_name: {}, ' \
               'path_name: {}, ' \
               'ctime: {}'.format(self.id, self.date_folder, self.file_path, self.file_name, self.path_name, self.ctime)


if __name__ == '__main__':
    pass
