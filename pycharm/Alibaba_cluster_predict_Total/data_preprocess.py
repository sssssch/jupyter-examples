#-*-coding:utf-8-*-
import pandas as pd

dataset = pd.read_csv(
    'machine_usage_headed.csv',
    index_col=1)
print(dataset.head())

dataset.drop('m_number', axis=1, inplace=True)
dataset.drop('mem_gps', axis=1, inplace=True)
dataset.drop('mpki', axis=1, inplace=True)
print(dataset.head())

dataset.columns = [
    'cpu_util_percent',
    'mem_util_percent',
    'net_in',
    'net_out',
    'disk_usage_percent']
dataset.index.name = 'Time'
print(dataset.head())


k = dataset.groupby('Time').mean()

#在这里，我取精确度为小数点前4位
k = round(k, 4)

k.to_csv('Machine_usage_groupby.csv')