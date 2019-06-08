#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-09
# Created by Author: czliuguoyu@163.com
import os
import time

# 配置文件的绝对路径
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    '''
    公共配置项
    '''

    # 是否开启定时任务
    SCHEDULER_API_ENABLED = True
    # 是否追踪对象的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否想控制台输出sql语句
    SQLALCHEMY_ECHO = False

    # 数据库连接
    DBS_CONN = 'mysql+pymysql://{user}:{pwd}@{url}:{port}/{name}?charset=utf8'

    now = time.localtime()

    # 定时任务指定
    JOBS = [
        # 每五分钟执行一次，获取实时价格信息
        {
            'id': 'now',
            'func': 'qtApp.controller.Price:now',
            'args': (),
            'trigger': 'interval',
            'minutes': 5
        },
        # 项目每85天执行一次，保证三个月内的数据完整
        {
            'id': 'history',
            'func': 'qtApp.controller.Price:history',
            'args': (),
            'trigger': 'interval',
            'days': 85
        }
    ]


class LocalConfig(Config):

    '''
    本地环境配置项
    '''

    # 环境名称
    ENV_NAME = 'local'
    # 是否开启debug模式
    DEBUG = True
    # aws接口地址
    AWS_REQUEST_ADDRESS = 'http://127.0.0.1:33333/ewd-agent'
    # 数据库用户名
    DB_USER = 'root'
    # 数据库密码
    DB_PWD = 'admin'
    # 数据库地址
    DB_URL = 'localhost'
    # 数据库端口号
    DB_PORT = 3306
    # 数据库名
    DB_NAME = 'spot_price'
    # 数据库连接
    DB_URL = Config.DBS_CONN.format(user=DB_USER, pwd=DB_PWD, url=DB_URL, port=DB_PORT, name=DB_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URL
    # 是否追踪对象的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 是否想控制台输出sql语句
    SQLALCHEMY_ECHO = True


class DevConfig(Config):

    '''
    开发环境配置项
    '''

    # 环境名称
    ENV_NAME = 'dev'
    # 是否开启debug模式
    DEBUG = False
    # aws接口地址
    AWS_REQUEST_ADDRESS = 'http://52.81.112.44:9009/ewd-agent'
    # 数据库用户名
    DB_USER = 'root'
    # 数据库密码
    DB_PWD = 'admin'
    # 数据库地址
    DB_URL = 'localhost'
    # 数据库端口号
    DB_PORT = 3306
    # 数据库名
    DB_NAME = 'ewd_test'
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = Config.DBS_CONN.format(user=DB_USER, pwd=DB_PWD, url=DB_URL, port=DB_PORT, name=DB_NAME)


class TestConfig(Config):

    '''
    测试环境配置项
    '''

    # 环境名称
    ENV_NAME = 'test'
    # 是否开启debug模式
    DEBUG = False
    # aws接口地址
    AWS_REQUEST_ADDRESS = 'http://52.81.112.44:9009/ewd-agent'
    # 数据库用户名
    DB_USER = 'root'
    # 数据库密码
    DB_PWD = 'admin'
    # 数据库地址
    DB_URL = 'localhost'
    # 数据库端口号
    DB_PORT = 3306
    # 数据库名
    DB_NAME = 'ewd_test'
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = Config.DBS_CONN.format(user=DB_USER, pwd=DB_PWD, url=DB_URL, port=DB_PORT, name=DB_NAME)


class ProductConfig(Config):

    '''
    正式环境配置项
    '''

    # 环境名称
    ENV_NAME = 'pro'
    # 是否开启debug模式
    DEBUG = False
    # aws接口地址
    AWS_REQUEST_ADDRESS = 'http://52.81.112.44:9009/ewd-agent'
    # 数据库用户名
    DB_USER = 'ewd-user'
    # 数据库密码
    DB_PWD = '8YM8FKZthjTVPX3n'
    # 数据库地址
    DB_URL = 'youcabdb.coyt2eoxywnh.rds.cn-north-1.amazonaws.com.cn'
    # 数据库端口号
    DB_PORT = 3306
    # 数据库名
    DB_NAME = 'ewd_data_collect'
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = Config.DBS_CONN.format(user=DB_USER, pwd=DB_PWD, url=DB_URL, port=DB_PORT, name=DB_NAME)


# 配置项字典设置
config = {
    'local': LocalConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'pro': ProductConfig,
    'default': LocalConfig
}


if __name__ == '__main__':
    pass
