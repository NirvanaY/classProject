#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from qtApp import db


class DBOperation(object):

    @staticmethod
    def add(entity):

        ''' 添加单条记录

        :param entity: 记录
        :return:
        '''

        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def add_all(entities):

        ''' 一次添加多条记录

        :param entities: 记录
        :return:
        '''

        db.session.add_all(entities)
        db.session.commit()


if __name__ == '__main__':
    pass
