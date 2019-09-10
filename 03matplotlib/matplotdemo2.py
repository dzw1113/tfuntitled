import matplotlib.pyplot as plt
import numpy as np
'''
figure 图像
'''

#多个窗口
#等差数列是指从第二项起，每一项与它的前一项的差等于同一个常数的一种数列，常用A、P表示。这个常数叫做等差数列的公差，公差常用字母d表示
#生成等差数列
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x

#定义第一个fig窗口
plt.figure()
plt.plot(x, y1)


#定义第二个窗口编号为3，大小为(8, 5)
plt.figure(num=4,figsize=(8,5))
plt.plot(x, y2)
plt.plot(x, y1,color='red',linewidth=10.0,linestyle='--')
plt.plot(5, 5,color='red',linewidth=10.0,linestyle='--')

plt.show()