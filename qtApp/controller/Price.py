#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
import datetime
import requests
from qtApp import scheduler
from flask import Blueprint
from concurrent.futures import ThreadPoolExecutor
from qtApp.views.Price import get_price_by_time
from qtApp.utils.DateUtil import get_timestamp
from qtApp.constant.AWSProperties import Region
from qtApp.result.CodeMsg import SUCCEES
from qtApp.utils.DateUtil import get_task_time

# 最多五个线程
executor = ThreadPoolExecutor(30)

# 创建蓝图信息
spotPrice = Blueprint('/price', __name__)


def now():

    ''' 执行定时任务，实时获取数据

    :return:
    '''

    requests.get('http://localhost:5000/price/now')


def history():

    ''' 执行定时任务，保证数据完整性

    :return:
    '''

    requests.get('http://localhost:5000/price/hisory')


def get():

    ''' 执行定时任务，保证数据完整性

    :return:
    '''

    requests.get('http://localhost:5000/price/get')


@spotPrice.route('/now')
def web_now():

    ''' 实时获取动态数据，不指定时间范围

    :return:
    '''

    # 获取北京区的时间
    executor.submit(get_price_by_time(None, None, Region.Beijing))
    # 获取宁夏区的时间
    executor.submit(get_price_by_time(None, None, Region.NingXia))

    return SUCCEES.msg


@spotPrice.route('/history')
def web_history():

    ''' 获取历史价格，保证数据完整

    :return:
    '''

    # 获取北京区的时间
    executor.submit(get_price_by_time(get_timestamp(85), get_timestamp(-1), Region.Beijing))
    # 获取宁夏区的时间
    executor.submit(get_price_by_time(get_timestamp(85), get_timestamp(-1), Region.NingXia))

    return SUCCEES.msg


@spotPrice.route('/get')
def get_price():

    ''' 获取历史价格记录

    :return:
    '''

    # 获取北京区的时间
    executor.submit(get_price_by_time(get_timestamp(100), get_timestamp(-1), Region.Beijing))
    # 获取宁夏区的时间
    executor.submit(get_price_by_time(get_timestamp(100), get_timestamp(-1), Region.NingXia))

    return 'SUCCESS'


# 定时任务
task = get_task_time()
scheduler.add_job(func=get, id='date', args=(), next_run_time=datetime.datetime(task.year, task.month, task.day,
                                                                                task.hour, task.minute, task.second))


if __name__ == '__main__':
    pass
