#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
import os


class OSUtil(object):

    @staticmethod
    def mkdir(path):

        ''' 创建文件夹

        :param path:
        :return:
        '''

        folder = os.path.exists(path)
        # 判断是否存在文件夹如果不存在则创建为文件夹
        if not folder:
            os.makedirs(path)


if __name__ == '__main__':
    pass
