# -*-coding:utf-8-*-
import pandas as pd
import csv

from pandas import concat

pd.options.display.expand_frame_repr = False

dataset = pd.read_csv(
    '/Users/mac/Downloads/task_usage_500_title.csv')
values = dataset.values
print(dataset.head())
dataset.drop('maximum_disk_io_time', axis=1, inplace=True)
dataset.drop('cpi', axis=1, inplace=True)
dataset.drop('aggregation_type', axis=1, inplace=True)
dataset.drop('sample_portion', axis=1, inplace=True)
print(dataset.head())

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

k = dataset.groupby('machine_id')
print(k.head())
