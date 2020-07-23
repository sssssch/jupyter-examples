# -*-coding:utf-8-*-
import pandas as pd
import numpy as np

dataset = pd.read_csv(
    'task_usage_500_title.csv')
values = dataset.values

dataset.drop('maximum_disk_io_time', axis=1, inplace=True)
dataset.drop('cpi', axis=1, inplace=True)
dataset.drop('aggregation_type', axis=1, inplace=True)
dataset.drop('sample_portion', axis=1, inplace=True)

dataset.columns = [
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
    'mai',
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
upcmu = dataset['unmapped_page_cache_memory_usage']
tpcmu = dataset['total_page_cache_memory_usage']
mmu = dataset['maximum_memory_usage']
mdit = dataset['mean_disk_io_time']
mldsu = dataset['mean_local_disk_space_used']
mcu = dataset['maximum_cpu_usage']
mai = dataset['mai']
scu = dataset['sampled_cpu_usage']

col_len = len(st)

# 取得end_time的最后一个数据，end_num
end_num = int(et[col_len - 1])

# 创建一个长度与数据长度相同的数组，作为cpu的储存器
cpu = [0] * (end_num - 600)
cmui = [0] * (end_num - 600)
amui = [0] * (end_num - 600)
upcmui = [0] * (end_num - 600)
tpcmui = [0] * (end_num - 600)
mmui = [0] * (end_num - 600)
mditi = [0] * (end_num - 600)
mldsui = [0] * (end_num - 600)
mcui = [0] * (end_num - 600)
maii = [0] * (end_num - 600)
scui = [0] * (end_num - 600)
# 将cpu循环赋值，需要以行为单位，将每一行的cpu信息添加至cpu数组中
# 这里的i代表着index
# 意味着我需要读取对应的第i行数据，再将其赋值到cpu对应的，从st到et的数组中
for i in range(0, col_len - 1):
    # 在这里，还需要将cpu的数组位置进行调整
    cpu[int(st[i]) - 600:int(et[i]) - 900] += mcur[i]
    cmui[int(st[i]) - 600:int(et[i]) - 900] += cmu[i]
    amui[int(st[i]) - 600:int(et[i]) - 900] += amu[i]
    upcmui[int(st[i]) - 600:int(et[i]) - 900] += upcmu[i]
    tpcmui[int(st[i]) - 600:int(et[i]) - 900] += tpcmu[i]
    mmui[int(st[i]) - 600:int(et[i]) - 900] += mmu[i]
    mditi[int(st[i]) - 600:int(et[i]) - 900] += mdit[i]
    mldsui[int(st[i]) - 600:int(et[i]) - 900] += mldsu[i]
    mcui[int(st[i]) - 600:int(et[i]) - 900] += mcu[i]
    maii[int(st[i]) - 600:int(et[i]) - 900] += mai[i]
    scui[int(st[i]) - 600:int(et[i]) - 900] += scu[i]

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
upcmui = list(map(lambda x: x * (end_num / 300) / col_len, upcmui))
tpcmui = list(map(lambda x: x * (end_num / 300) / col_len, tpcmui))
mmui = list(map(lambda x: x * (end_num / 300) / col_len, mmui))
mditi = list(map(lambda x: x * (end_num / 300) / col_len, mditi))
mldsui = list(map(lambda x: x * (end_num / 300) / col_len, mldsui))
mcui = list(map(lambda x: x * (end_num / 300) / col_len, mcui))
maii = list(map(lambda x: x * (end_num / 300) / col_len, maii))
scui = list(map(lambda x: x * (end_num / 300) / col_len, scui))
print(cpu)

list = np.zeros((11, (end_num - 600)))
list[0] = cpu
list[1] = cmui
list[2] = amui
list[3] = upcmui
list[4] = tpcmui
list[5] = mmui
list[6] = mditi
list[7] = mldsui
list[8] = mcui
list[9] = maii
list[10] = scui

np.savetxt("test.csv", list, delimiter=',')




