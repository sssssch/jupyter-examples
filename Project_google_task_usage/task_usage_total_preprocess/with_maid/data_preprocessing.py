# -*-coding:utf-8-*-

import pandas as pd
import numpy as np
from numpy import *
import pandas

name = [
    'start_time',
    'end_time',
    'job_id',
    'task_index',
    'machine_id',
    'mean_cpu_usage_rate',
    'canonical_memory_usage',
    'assigned_memory_usage',
    'unmapped_page_cache_memory_usage',
    'total_page_cache_memory_usage',
    'maximum_memory_usage',
    'mean_disk_io_time',
    'mean_local_disk_space_used',
    'maximum_cpu_usage',
    'maximum_disk_io_time',
    'cpi',
    'mai',
    'sample_portion',
    'aggregation_type',
    'sampled_cpu_usage']

dataset = pd.read_csv(
    'task_usage.csv',
    header=None,
    names=name,
    nrows=100000000)

dataset.drop('maximum_disk_io_time', axis=1, inplace=True)
dataset.drop('cpi', axis=1, inplace=True)
dataset.drop('aggregation_type', axis=1, inplace=True)
dataset.drop('sample_portion', axis=1, inplace=True)
dataset.drop('mai', axis=1, inplace=True)
dataset.drop('unmapped_page_cache_memory_usage', axis=1, inplace=True)
dataset.drop('job_id', axis=1, inplace=True)
dataset.drop('task_index', axis=1, inplace=True)

dataset.columns = [
    'start_time',
    'end_time',
    'machine_id',
    'mean_cpu_usage_rate',
    'canonical_memory_usage',
    'assigned_memory_usage',
    'total_page_cache_memory_usage',
    'maximum_memory_usage',
    'mean_disk_io_time',
    'mean_local_disk_space_used',
    'maximum_cpu_usage',
    'sampled_cpu_usage']

# 定义时间单位为min
st = dataset['start_time']
et = dataset['end_time']

# 转化min,第一组时间为5min-10min,时间间隔为5min
st /= 60000000
et /= 60000000


# 获得整个数据的列数col_len
col_len = len(st)
# 取得end_time的最后一个数据，end_num
end_num = int(et[col_len - 1])


def data_round(num):
    singled = num // 5
    if num % 5 != 0:
        singled += 1
    return singled * 5


# 在这里，将st与et转化成间隔为5的两列数据
for i in range(0, col_len - 1):
    st[i] = data_round(st[i])
    et[i] = data_round(et[i])

# 赋值回去
dataset['start_time'] = st
dataset['end_time'] = et
print(dataset.head())

# 现在的dataset变动了时间（st,et)部分，保留了maid以及9个预测值
# 下一步，需要将maid进行分类，使用groupby
k = dataset.groupby(['start_time', 'end_time', 'machine_id']).sum()
k.to_csv('task_usage_preprocessed_ud.csv')