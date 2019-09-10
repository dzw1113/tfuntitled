# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
'''
设置坐标轴2
'''
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


#使用plt.gca获取当前坐标轴信息. 使用.spines设置边框;右侧边框；
# 使用.set_color设置边框颜色：默认白色；
# 使用.spines设置边框：上边框；使用.set_color设置边框颜色：默认白色；
#隐去右边和上边的线
ax = plt.gca();
ax.spines['right'].set_color('none');
ax.spines['top'].set_color('none')

#使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom.（所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('bottom');
#使用.yaxis.set_ticks_position设置y坐标刻度数字或名称的位置：left.（所有位置：left，right，both，default，none）
ax.yaxis.set_ticks_position('left');

#使用.spines设置边框：x轴；使用.set_position设置边框位置：y=-1的位置；（位置所有属性：outward，axes，data）
ax.spines['bottom'].set_position(('data',-1));
ax.spines['left'].set_position(('data',0.5))

plt.show()