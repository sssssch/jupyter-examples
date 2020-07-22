# -*-coding:utf-8-*-
import pandas as pd

dataset = pd.read_csv(
    '/Users/mac/Downloads/task_usage_500_title.csv')
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
col_len = len(st)

# 取得end_time的最后一个数据，end_num
end_num = int(et[col_len - 1])

# 创建一个长度与数据长度相同的数组，作为cpu的储存器
cpu = [0] * (end_num - 600)

# 将cpu循环赋值，需要以行为单位，将每一行的cpu信息添加至cpu数组中
# 这里的i代表着index
# 意味着我需要读取对应的第i行数据，再将其赋值到cpu对应的，从st到et的数组中
for i in range(0, col_len - 1):
    # 在这里，还需要将cpu的数组位置进行调整
    cpu[int(st[i]) - 600:int(et[i]) - 900] += mcur[i]

# 在这里，我将对生成的cpu数据进行划分，使得cpu = cpui / 当前时刻工作机器数量
for i in range(0, col_len - 1):
    total_com = 0
    for j in range(0, col_len - 1):
        if (int(st[j]) - 600) <= i <= (int(et[j]) - 600):  # end_time != start_time
            total_com += 1
    cpu[i] = cpu[i] / total_com
    
print(cpu)
