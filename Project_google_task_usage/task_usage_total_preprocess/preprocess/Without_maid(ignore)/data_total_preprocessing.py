# -*-coding:utf-8-*-

import pandas as pd
import numpy as np
from numpy import *

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
    nrows=15000000)



dataset.drop('maximum_disk_io_time', axis=1, inplace=True)
dataset.drop('cpi', axis=1, inplace=True)
dataset.drop('aggregation_type', axis=1, inplace=True)
dataset.drop('sample_portion', axis=1, inplace=True)
dataset.drop('mai', axis=1, inplace=True)
dataset.drop('unmapped_page_cache_memory_usage', axis=1, inplace=True)

dataset.columns = [
    'start_time',
    'end_time',
    'job_id',
    'task_index',
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
print(dataset.head())

# 确定最小时间单位
# k = dataset.groupby('start_time').mean()
# print(k.head())
# 确定了最小的时间间隔为1000000，所以将整个st与et除以1000000

# 获得数据的长度
st = dataset['start_time']
et = dataset['end_time']

# st，et转化为最小时间间隔
st = st / 1000000
et = et / 1000000
mcur = dataset['mean_cpu_usage_rate']
cmu = dataset['canonical_memory_usage']
amu = dataset['assigned_memory_usage']
tpcmu = dataset['total_page_cache_memory_usage']
mmu = dataset['maximum_memory_usage']
mdit = dataset['mean_disk_io_time']
mldsu = dataset['mean_local_disk_space_used']
mcu = dataset['maximum_cpu_usage']
scu = dataset['sampled_cpu_usage']

col_len = len(st)

# 取得end_time的最后一个数据，end_num
end_num = int(et[col_len - 1])

# 创建一个长度与数据长度相同的数组，作为cpu的储存器
en_mat_lenth = end_num - 600
cpu = [0] * en_mat_lenth
cmui = [0] * en_mat_lenth
amui = [0] * en_mat_lenth
tpcmui = [0] * en_mat_lenth
mmui = [0] * en_mat_lenth
mditi = [0] * en_mat_lenth
mldsui = [0] * en_mat_lenth
mcui = [0] * en_mat_lenth
scui = [0] * en_mat_lenth
# 将cpu循环赋值，需要以行为单位，将每一行的cpu信息添加至cpu数组中
# 这里的i代表着index
# 意味着我需要读取对应的第i行数据，再将其赋值到cpu对应的，从st到et的数组中
for i in range(0, col_len - 1):
    # 在这里，还需要将cpu的数组位置进行调整
    isti_600 = int(st[i]) - 600
    ieti_900 = int(2 * et[i] - st[i] - 900)
    cpu[isti_600:ieti_900] += mcur[i]
    cmui[isti_600:ieti_900] += cmu[i]
    amui[isti_600:ieti_900] += amu[i]
    tpcmui[isti_600:ieti_900] += tpcmu[i]
    mmui[isti_600:ieti_900] += mmu[i]
    mditi[isti_600:ieti_900] += mdit[i]
    mldsui[isti_600:ieti_900] += mldsu[i]
    mcui[isti_600:ieti_900] += mcu[i]
    scui[isti_600:ieti_900] += scu[i]

# 在这里，我将对生成的cpu数据进行划分，使得cpu = cpui / 当前时刻工作机器数量
# for i in range(0, col_len - 1):
#     total_com = 0
#     for j in range(0, col_len - 1):
#         if (int(st[j]) - 600) <= i <= (int(et[j]) - 600):  # end_time != start_time
#             total_com += 1
#     cpu[i] = cpu[i] / total_com

# 在这里我做了简化，对于一个服务器而言，所有时刻的请求总量在大体上是相同的
cpu = list(map(lambda x: x * (end_num / 300) / col_len, cpu))
cmui = list(map(lambda x: x * (end_num / 300) / col_len, cmui))
amui = list(map(lambda x: x * (end_num / 300) / col_len, amui))
tpcmui = list(map(lambda x: x * (end_num / 300) / col_len, tpcmui))
mmui = list(map(lambda x: x * (end_num / 300) / col_len, mmui))
mditi = list(map(lambda x: x * (end_num / 300) / col_len, mditi))
mldsui = list(map(lambda x: x * (end_num / 300) / col_len, mldsui))
mcui = list(map(lambda x: x * (end_num / 300) / col_len, mcui))
scui = list(map(lambda x: x * (end_num / 300) / col_len, scui))

lissi = np.zeros((9, (end_num - 600)))
lissi[0] = cpu
lissi[1] = cmui
lissi[2] = amui
lissi[3] = tpcmui
lissi[4] = mmui
lissi[5] = mditi
lissi[6] = mldsui
lissi[7] = mcui
lissi[8] = scui

# np.savetxt("test.csv", lissi, delimiter=',')

dataset = np.round(lissi, 8)
List_data = mat(dataset)
Inverse = List_data.T
name = [
    'cpu',
    'cmui',
    'amui',
    'tpcmui',
    'mmui',
    'mditi',
    'mldsui',
    'mcui',
    'scui'
]

test = pd.DataFrame(columns=name, data=Inverse)
test.to_csv(
    'task_usage_total_inversed_bycode.csv',
    encoding='gbk')
