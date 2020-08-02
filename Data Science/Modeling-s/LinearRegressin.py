#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    LinearRegressin.py
# @Author:      manunellutla
# @Time:        8/1/20 10:59 PM

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

df = pd.read_csv('../Data/melb_data2.csv')

print(df.columns)
print(df.dtypes)
#print(df.isnull().any())

y = df['Price'].values
X = df['Rooms'].values
X=X.reshape(-1,1)

model = LinearRegression()
model.fit(X, y)
plt.scatter(X, y,color='r')

plt.plot(X, model.predict(X),color='k')

plt.show()