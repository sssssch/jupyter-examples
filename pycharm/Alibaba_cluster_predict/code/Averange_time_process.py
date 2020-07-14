#-*-coding:utf-8-*-
#groupby函数的简单快捷，一个函数就包括了众多循环，大大节省了时间。


import pandas as pd

dataset = pd.read_csv(
    '/Users/mac/Downloads/深度学习资料/Multivariable_LSTM/Alibaba_cluster_predict/data/Machine_usage_fill.csv')

k = dataset.groupby('Time').mean()

#在这里，我取精确度为小数点前4位
k = round(k, 4)
print(k.head())

k.to_csv('Machine_usage_groupby.csv')

