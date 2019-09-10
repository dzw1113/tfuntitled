# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
'''
Contours 等高线图
'''
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
#meshgrid生成网格值
X,Y = np.meshgrid(x, y)


plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
#开始画等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())

plt.show();