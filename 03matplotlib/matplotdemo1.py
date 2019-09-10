import matplotlib.pyplot as plt
import numpy as np
'''
基本用法
'''

#等差数列是指从第二项起，每一项与它的前一项的差等于同一个常数的一种数列，常用A、P表示。这个常数叫做等差数列的公差，公差常用字母d表示
#生成等差数列
x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.figure()
plt.plot(x, y)
plt.show()