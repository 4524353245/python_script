import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
# 文件路径
path = "C:\\Users\\surface\Desktop\\2018 APMCM Problems\\2018 APMCM Problem A\\Annex 2 raw data\\"
data = pd.read_csv(path+'baiqingquan_g9.trc',sep='\t')
shape = data.shape
# print(shape)
x = []
y = []
z = []
# 向列表中填入数据
for i in range(0,shape[0]):
    # 依次读取一行数据
    column =data.loc[i].values
    for items in range(2,shape[1]-3,3):
        x.append(column[items])
        y.append(column[items+1])
        z.append(column[items+3])
# print(len(x))       

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.ion()                  # 开启一个画图的窗口    
for i in range(0,9786):
    ax.scatter(x[i], y[i], z[i])
    if i % 42 == 0 and i is not 0:
        plt.show()
        plt.pause(0.01)         # 暂停一秒
        # plt.clf()  # 清除当前 figure 的所有axes，但是不关闭这个 window，所以能继续复用于其他的 plot。
        plt.cla() # 清除axes，即当前 figure 中的活动的axes，但其他axes保持不变。

