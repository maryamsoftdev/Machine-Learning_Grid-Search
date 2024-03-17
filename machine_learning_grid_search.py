# -*- coding: utf-8 -*-
"""Machine Learning - Grid Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17vPC9LUL0mNIbgCPByiny_qx4g7D2V-c
"""

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris['data']
y = iris['target']

logit = LogisticRegression(max_iter = 10000)

print(logit.fit(X,y))

print(logit.score(X,y))
#With the default setting of C = 1, we achieved a score of 0.973.

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
#First we will create an empty list to store the score withi
scores = []
#To change the values of C we must loop over the range of values and update the parameter each time.
for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))

  print(scores)