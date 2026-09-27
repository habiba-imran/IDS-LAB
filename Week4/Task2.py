# How to convert the categorical data into numeric data in python by using Pandas?
import pandas as pd
data = pd.read_csv('Week4/Train.csv')
data['code'] = pd.factorize(data.Item_Fat_Content)[0]
print(data.head())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['code'] = le.fit_transform(data.Item_Fat_Content)
print(data.head())
