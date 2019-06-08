#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-09
# Created by Author: czliuguoyu@163.com
from config import config
from qtApp import create_app, db


def create_tables(my_app):

    ''' 创建数据表

    :param my_app: 项目app
    :return:
    '''

    # 为了确保数据表自动创建成功
    # 需要在指定db.create_all()的时候先导入数据表
    from qtApp.entity import PriceBj, PriceNx, SystemDict, RecordCSV
    # 创建所有的数据表
    db.create_all(app=my_app)


if __name__ == '__main__':

    # 读取配置文件
    app = create_app(config['local'])
    app.app_context().push()

    # 创建所有数据表
    create_tables(app)

    app.run()
