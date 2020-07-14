# -*-coding:utf-8-*-

import datetime
import pandas as pd
pd.options.display.expand_frame_repr = False

dataset = pd.read_csv(
    '/Users/mac/Downloads/深度学习资料/Multivariable_LSTM/Alibaba_cluster_predict/data/machine_usage_50000.csv')
values = dataset.values

print(dataset.head())

# 指定索引项
dataset = pd.read_csv(
    '/Users/mac/Downloads/深度学习资料/Multivariable_LSTM/Alibaba_cluster_predict/data/machine_usage_50000.csv',
    index_col=1)
print(dataset.head())
dataset.drop('m_number', axis=1, inplace=True)
print(dataset.head())

dataset.columns = [
    'cpu_util_percent',
    'mem_util_percent',
    'mem_gps',
    'mpki',
    'net_in',
    'net_out',
    'disk_usage_percent']
dataset.index.name = 'Time'

dataset['mem_gps'].fillna(0, inplace=True)
dataset['mpki'].fillna(0, inplace=True)

print(dataset.head())

dataset.to_csv('Machine_usage_fill.csv')
