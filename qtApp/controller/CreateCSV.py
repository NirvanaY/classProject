#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from flask import Blueprint
from qtApp.views.Price import create_csv_records

# 创建蓝图信息
csv = Blueprint('/csv', __name__)


@csv.route('create')
def getlist():

    ''' 定时生成CSV文件

    :return:
    '''
    create_csv_records()
    return 'SUCCESS'


if __name__ == '__main__':
    pass
