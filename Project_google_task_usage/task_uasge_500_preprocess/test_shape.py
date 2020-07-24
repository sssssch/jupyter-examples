# -*-coding:utf-8-*-
import numpy as np

end_num = 700
list = np.zeros((11, (end_num - 600)))
print(list.shape)
print(list[0])

np.savetxt("test.csv", list, delimiter=',')
