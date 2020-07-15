# -*-coding:utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt

# pd.options.display.expand_frame_repr = False

dataset = pd.read_csv(
    '/Users/mac/Downloads/深度学习资料/Multivariable_LSTM/Alibaba_cluster_predict/data/Machine_usage_groupby.csv')

values = dataset.values
groups = [1, 2, 3, 5, 6, 7]

i = 1
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(values[:, 0], values[:, group])
    plt.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
plt.show()

print(dataset.head())