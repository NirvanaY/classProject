#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-10
# Created by Author: czliuguoyu@163.com
import time
import datetime
from qtApp.constant.ParamsName import TimeFormatString


def format_greenwich(time_str: str) -> int:

    ''' 把数据请求获取的格林威治时间改为+8时区

    :param time_str: 格林威治时间字符串
    :return:
    '''

    # 将格林威治时间字符串转为datetime类型
    date_time = datetime.datetime.strptime(time_str, TimeFormatString.GREENWICH)
    # 将时间转为+8时区
    record_time = date_time + datetime.timedelta(hours=8)
    # 获取时间戳
    timestamp = int(time.mktime(record_time.timetuple())) * 1000

    return timestamp


def get_timestamp(days):

    ''' 获取时间戳

    :param days: 当前时间的偏移量
                 正数向前偏移，负数向后偏移
    :return:
    '''

    format_time = datetime.datetime.today() - datetime.timedelta(days=days)
    return int(time.mktime(format_time.timetuple())) * 1000


def get_task_time():

    ''' 获取执行获取历史价格方法的时间

    :return:
    '''

    return datetime.datetime.today() - datetime.timedelta(minutes=-10)


if __name__ == '__main__':
    pass
