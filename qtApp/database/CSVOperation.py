#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from qtApp.database.DBOperation import DBOperation
from qtApp.entity.RecordCSV import RecordCSV


class CSVOperation(DBOperation):

    @staticmethod
    def find_csv_records(date_folder):

        ''' 根据时间查找每天的csv文件记录

        :return:
        '''
        return RecordCSV.query.filter_by(date_folder=date_folder).all()


if __name__ == '__main__':
    pass
