#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    RNNLSTMSenti.py
# @Author:      manunellutla
# @Time:        8/19/20 7:27 PM

from tensorflow.keras.models import load_model


def rnn_lstm_senti_analysis(txt: str):
    modl = load_model('rnn-lstm-senti.h5')
    score = modl.evaluate(txt)
    return score


if __name__ == '__main__':
    res = rnn_lstm_senti_analysis("I am very Happy")
    print(res)
