# -*-coding:utf-8-*-

import pandas as pd
df = pd.read_csv('machine_usage.csv', header=0)
print(df.head())
df.columns = [
    'm_number',
    'Time',
    'cpu_util_percent',
    'mem_util_percent',
    'mem_gps',
    'mpki',
    'net_in',
    'net_out',
    'disk_usage_percent']
print(df.head())
df.to_csv('machine_usage_headed.csv', index=False)
