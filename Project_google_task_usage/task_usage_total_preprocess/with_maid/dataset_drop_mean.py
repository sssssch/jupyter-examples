#-*-coding:utf-8-*-

import pandas as pd
import numpy as np
from numpy import *
import pandas

k = pd.read_csv(
    'task_usage_preprocessed_ud.csv')

k.drop('end_time', axis=1, inplace=True)
k.drop('machine_id', axis=1, inplace=True)
k = np.round(k, 8)
print(k.head())

# 现在的数据集，包含了st，et，以及需要求的9个预测量
# 在这一步，求平均值，得到以开始时间段作为参数的预测量平均值
k = k.groupby(['start_time']).mean()
k.to_csv('task_usage_preprocessed.csv')
