# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:11:16 2025

@author: mkamr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv("C:\\Users\\mkamr\\Train.csv")
for c in train.columns[:-1]:
    plt.scatter(train[c], train['TYPE'])
    plt.xlabel(c)
    plt.ylabel('TYPE')
    plt.show()

test = pd.read_csv("C:\\Users\\mkamr\\Test.csv")
X = train.drop('TYPE', axis=1).values
y = train['TYPE'].values
Xt = test.values
pred_labels = []
for t in Xt:
    d = np.sqrt(((X - t) ** 2).sum(axis=1))
    idx = np.argmin(d)
    pred_labels.append(y[idx])
test['TYPE'] = pred_labels
test.to_csv("C:\\Users\\mkamr\\Predicted.csv", index=False)
print(test)