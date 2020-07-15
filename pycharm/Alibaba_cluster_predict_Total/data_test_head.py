#-*-coding:utf-8-*-\


# head -100 Machine_usage_groupby.csv >Machine_usage_groupby_100.csv
import pandas as pd

dataset = pd.read_csv(
    'Machine_usage_groupby_100.csv')

print(dataset.head())


