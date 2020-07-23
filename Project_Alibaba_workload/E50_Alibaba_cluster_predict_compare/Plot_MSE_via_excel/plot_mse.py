#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv(
    '/Users/mac/Downloads/Plot_MSE_via_Matlab/mse_plot.csv',
    header = None,
    names = ['x', 'value'])
data = pd.DataFrame(file)
# 数组切片
x = data['x']  # 取第一列数据
y = data['value']  # 取第二列数据
plt.xlim((0, 60))
plt.plot(x,y)
plt.savefig('out3.png',dpi=600)
# 设置需要保存图片的分辨率
plt.show()

