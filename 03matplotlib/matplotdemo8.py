# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
'''
Scatter 散点图
'''
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


n = 1024;#data size

X = np.random.normal(0,1,n);#生成1024给X数据
Y = np.random.normal(0,1,n);#生成1024给Y数据
T = np.arctan2(Y,X);#并图像化这个数据集

#输入X和Y作为location，size=75，颜色为T，color map用默认值，透明度alpha 为 50%。
plt.scatter(X,Y,s=75,c=T,alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()
