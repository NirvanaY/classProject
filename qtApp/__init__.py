#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-09
# Created by Author: czliuguoyu@163.com
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

# 数据库拓展
db = SQLAlchemy()

# 定时任务
scheduler = APScheduler()


def create_app(config):

    ''' app创建工厂

    :param config:
    :return:
    '''

    # 实例化app
    app = Flask(__name__)
    # 配置文件
    app.config.from_object(config)

    # 初始化数据库
    db.init_app(app)

    # 初始化定时任务
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        # 防止方式任务执行两次
        scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    from qtApp.controller.Price import spotPrice
    from qtApp.controller.CreateCSV import csv
    from qtApp.controller.TrainModel import model
    app.register_blueprint(spotPrice, url_prefix='/price')
    app.register_blueprint(csv, url_prefix='/csv')
    app.register_blueprint(model, url_prefix='/model')

    return app


if __name__ == '__main__':
    pass
