#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-23
# Created by Author: czliuguoyu@163.com
from __future__ import print_function
import time
import tensorflow as tf
from tensorflow.contrib.timeseries.python.timeseries import estimators as ts_estimators
import matplotlib.pyplot as plt
from qtApp.database.CSVOperation import CSVOperation
from qtApp.utils.OSUtil import OSUtil
from qtApp.train.LSTM import _LSTMModel


def read_csv():

    ''' 使用tf读入待训练数据

    :return:
    '''

    paths = get_paths()

    for path in paths:

        reader = tf.contrib.timeseries.CSVReader(path)
        train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(reader, batch_size=4, window_size=100)

        estimator = ts_estimators.TimeSeriesRegressor(model=_LSTMModel(num_features=1, num_units=7),
                                                      optimizer=tf.train.AdamOptimizer(0.001))

        estimator.train(input_fn=train_input_fn, steps=2000)
        evaluation_input_fn = tf.contrib.timeseries.WholeDatasetInputFn(reader)
        evaluation = estimator.evaluate(input_fn=evaluation_input_fn, steps=1)
        (predictions,) = tuple(estimator.predict(
            input_fn=tf.contrib.timeseries.predict_continuation_input_fn(evaluation, steps=20)))

        observed_times = evaluation["times"][0]
        observed = evaluation["observed"][0, :, :]
        evaluated_times = evaluation["times"][0]
        evaluated = evaluation["mean"][0]
        predicted_times = predictions['times']
        predicted = predictions["mean"]

        image_path = './pre_image/{date}/'.format(date=time.strftime("%Y-%m-%d", time.localtime()))
        OSUtil.mkdir(image_path)

        plt.figure(figsize=(15, 5))
        plt.axvline(999, linestyle="dotted", linewidth=4, color='r')
        observed_lines = plt.plot(observed_times, observed, label="observation", color="k")
        evaluated_lines = plt.plot(evaluated_times, evaluated, label="evaluation", color="g")
        predicted_lines = plt.plot(predicted_times, predicted, label="prediction", color="r")
        plt.legend(handles=[observed_lines[0], evaluated_lines[0], predicted_lines[0]], loc="upper left")
        plt.savefig(image_path+path.spilt('/')[3].split('.')[0]+'.png')


def get_paths():

    ''' 从数据库中获取csv文件存放地址

    :return:
    '''

    # 根据时间查询csv生成记录
    records = CSVOperation.find_csv_records(date_folder=time.strftime("%Y-%m-%d", time.localtime()))
    # 提取路劲
    csv_path_list = []
    for record in records:
        csv_path_list.append(record.path_name)

    return csv_path_list


if __name__ == '__main__':
    pass
