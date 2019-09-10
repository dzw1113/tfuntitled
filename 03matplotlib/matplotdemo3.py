# -*- coding:utf-8 -*-
'''
设置坐标轴1
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

#----设置x轴的取值范围
plt.xlim((-1, 5))
plt.ylim((-2, 3))
#描述X,Y
plt.xlabel(u'我是x轴')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
#把X轴的-1到5换成当前新的刻度
plt.xticks(new_ticks)

plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

plt.show()