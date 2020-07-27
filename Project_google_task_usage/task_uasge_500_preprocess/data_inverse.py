# -*-coding:utf-8-*-
import pandas as pd
from numpy import *

dataset = pd.read_csv(
    'test_data.csv', header=None)
dataset = round(dataset, 8)
List_data = mat(dataset)
Inverse = List_data.T
print(Inverse)
name = [
    'cpu',
    'cmui',
    'amui',
    'upcmui',
    'tpcmui',
    'mmui',
    'mditi',
    'mldsui',
    'mcui',
    'scui'
]

test = pd.DataFrame(columns=name, data=Inverse)
test.to_csv('test_data_inversed_bycode.csv', encoding='gbk', header=None)
