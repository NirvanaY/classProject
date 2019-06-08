#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from qtApp.database.DBOperation import DBOperation
from qtApp.entity.SystemDict import SystemDict


class SysDict(DBOperation):

    @staticmethod
    def find_by_column_type(column_type):

        ''' 通过字段类型查找所有的字典值

        :param column_type:
        :return:
        '''
        return SystemDict.query.filter_by(column_type=column_type).all()

    @staticmethod
    def find_by_value_type(value_type):

        ''' 通过字段值查找对应的字典值

        :param value_type:
        :return:
        '''
        return SystemDict.query.filter_by(value_type=value_type).all()


if __name__ == '__main__':
    pass
