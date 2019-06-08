#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from flask import Blueprint
from qtApp.views.ModelTrain import read_csv

# 创建蓝图信息
model = Blueprint('/model', __name__)


@model.route('read')
def read():
    read_csv()
    return "SUCCEED"


if __name__ == '__main__':
    pass
