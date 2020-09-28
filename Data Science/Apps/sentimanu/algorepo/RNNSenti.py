#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    RNNSenti.py
# @Author:      manunellutla
# @Time:        8/18/20 9:33 PM

"""
    This program creates the model which was trained
"""

import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.layers import Embedding, LSTM, Dense
from tensorflow.python.keras.models import Sequential

colnames = ['sentence', 'target']
amz_review = pd.read_csv('amazon_cells_labelled.txt', sep='\t', names=colnames)

# print(amz_review.head())
# print(amz_review.info())
# print(amz_review['target'].value_counts())

X, y = (amz_review['sentence'].values, amz_review['target'].values)  # RNN input requires array data type

tk = Tokenizer(lower=True)
tk.fit_on_texts(X)
X_seq = tk.texts_to_sequences(X)
X_pad = pad_sequences(X_seq, maxlen=20, padding='post')

X_train, X_test, y_train, y_test = train_test_split(X_pad, y, test_size=0.20, random_state=0)

# RNN with LSTM
model = Sequential()
model.add(Embedding(input_dim=len(tk.word_counts.keys()) + 1, output_dim=128, input_length=20))
model.add(LSTM(units=200, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=50, epochs=30)

print(model.summary())

scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

model.save('rnn-lstm-senti.h5')