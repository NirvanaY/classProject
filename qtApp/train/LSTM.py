#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019-05-24
# Created by Author: czliuguoyu@163.com
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow.contrib.timeseries.python.timeseries import model as ts_model


class _LSTMModel(ts_model.SequentialTimeSeriesModel):

    '''
        重写LSTMModel类
    '''

    def __init__(self, num_units, num_features, dtype=tf.float32):

        super(_LSTMModel, self).__init__(train_output_names=["mean"],
                                         predict_output_names=["mean"],
                                         num_features=num_features,
                                         dtype=dtype)

        self._num_units = num_units
        self._lstm_cell = None
        self._lstm_cell_run = None
        self._predict_from_lstm_output = None

    def initialize_graph(self, input_statistics):

        super(_LSTMModel, self).initialize_graph(input_statistics=input_statistics)

        self._lstm_cell = tf.nn.rnn_cell.LSTMCell(num_units=self._num_units)

        self._lstm_cell_run = tf.make_template(name_="lstm_cell", func_=self._lstm_cell, create_scope_now_=True)
        self._predict_from_lstm_output = tf.make_template(name_="predict_from_lstm_output",
                                                          func_=lambda inputs: tf.layers.dense(inputs=inputs,
                                                                                               units=self.num_features),
                                                          create_scope_now_=True)

    def get_start_state(self):

        return (tf.zeros([], dtype=tf.int64),
                tf.zeros([self.num_features], dtype=self.dtype),
                [tf.squeeze(state_element, axis=0) for state_element
                 in self._lstm_cell.zero_state(batch_size=1, dtype=self.dtype)])

    def _transform(self, data):

        mean, variance = self._input_statistics.overall_feature_moments
        return (data - mean) / variance

    def _de_transform(self, data):

        mean, variance = self._input_statistics.overall_feature_moments
        return data * variance + mean

    def _filtering_step(self, current_times, current_values, state, predictions):

        state_from_time, prediction, lstm_state = state

        with tf.control_dependencies([tf.assert_equal(current_times, state_from_time)]):
            transformed_values = self._transform(current_values)
            predictions["loss"] = tf.reduce_mean(
                (prediction - transformed_values) ** 2, axis=-1)
            new_state_tuple = (current_times, transformed_values, lstm_state)

        return (new_state_tuple, predictions)

    def _prediction_step(self, current_times, state):

        _, previous_observation_or_prediction, lstm_state = state

        lstm_output, new_lstm_state = self._lstm_cell_run(inputs=previous_observation_or_prediction,
                                                          state=lstm_state)

        next_prediction = self._predict_from_lstm_output(lstm_output)
        new_state_tuple = (current_times, next_prediction, new_lstm_state)

        return new_state_tuple, {"mean": self._de_transform(next_prediction)}

    def _imputation_step(self, current_times, state):

        return state

    def _exogenous_input_step(self, current_times, current_exogenous_regressors, state):

        raise NotImplementedError("Exogenous inputs are not implemented for this example.")


if __name__ == '__main__':
    pass
