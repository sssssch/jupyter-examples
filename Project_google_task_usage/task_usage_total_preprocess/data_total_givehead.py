# -*-coding:utf-8-*-
import pandas as pd
df = pd.read_csv('task_usage.csv', header=0)

df.columns = [
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
df.to_csv('task_usage_headed.csv', index=False)
