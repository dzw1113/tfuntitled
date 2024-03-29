import numpy as np

print("NumPy简单入门教程:https://www.numpy.org.cn/article/basics/an_introduction_to_scientific_python_numpy.html")

print('数组基础')

print('创建一个数组:ndarrays。创建数组的4种不同方法，基本的方法是将序列传递给NumPy的array()函数; 你可以传递任何序列（类数组），而不仅仅是常见的列表（list）数据类型')

# 1D Array 一维数组
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print(a) # >>>[0 1 2 3 4]
print(b) # >>>[0 1 2 3 4]
print(c) # >>>[0 1 2 3 4]
print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[3]) # >>>3

print()
print('创建一个2D（二维）数组')
# MD Array,
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[2,4]) # >>>25


#它背后的一些数学知识
# 要正确理解这一点，我们应该真正了解一下矢量和矩阵是什么。
#
# 矢量是具有方向和幅度的量。它们通常用于表示速度，加速度和动量等事物。向量可以用多种方式编写，尽管对我们最有用的是它们被写为n元组的形式，如（1,4,6,9）。这就是我们在NumPy中表示他们的方式。
#
# 矩阵类似于矢量，除了它由行和列组成; 很像一个网格。可以通过给出它所在的行和列来引用矩阵中的值。在NumPy中，我们通过传递一系列序列来制作数组，就像我们之前所做的那样。


print()
print('#多维数组切片')
print(a)
print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]

print()
print('#数组属性')

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2
print(a.nbytes) # >>>200

# 正如你在上面的代码中看到的，NumPy数组实际上被称为ndarray。我不知道为什么他妈的它叫ndarray，如果有人知道请留言！我猜它代表n维数组。
#
# 数组的形状是它有多少行和列，上面的数组有5行和5列，所以它的形状是(5，5)。
#
# itemsize属性是每个项占用的字节数。这个数组的数据类型是int 64，一个int 64中有64位，一个字节中有8位，除以64除以8，你就可以得到它占用了多少字节，在本例中是8。
#
# ndim 属性是数组的维数。这个有2个。例如，向量只有1。
#
# nbytes 属性是数组中的所有数据消耗掉的字节数。你应该注意到，这并不计算数组的开销，因此数组占用的实际空间将稍微大一点。

print()
print('#使用数组')
#基本操作符
# 只是能够从数组中创建和检索元素和属性不能满足你的需求，你有时也需要对它们进行数学运算。 你完全可以使用四则运算符 +、- 、/ 来完成运算操作。

# Basic Operators
a = np.arange(25)
a = a.reshape((5, 5))

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2) # a数组的平方
print(a < b)

print(a > b)

print(a.dot(b))

# 除了 dot() 之外，这些操作符都是对数组进行逐元素运算。比如 (a, b, c) + (d, e, f) 的结果就是 (a+d, b+e, c+f)。
# 它将分别对每一个元素进行配对，然后对它们进行运算。它返回的结果是一个数组。注意，当使用逻辑运算符比如 “<” 和 “>” 的时候，返回的将是一个布尔型数组，这点有一个很好的用处，后边我们会提到。
#
# dot() 函数计算两个数组的点积。它返回的是一个标量（只有大小没有方向的一个值）而不是数组。

#它背后的一些数学知识
# dot()函数称为点积。理解这一点的最好方法是看下图，下图将表示它是如何进行计算的。


print()
print('#数组特殊运算符')

# NumPy还提供了一些别的用于处理数组的好用的运算符。
# dot, sum, min, max, cumsum
a = np.arange(10)
print(a)

print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]

# sum()、min()和max()函数的作用非常明显。将所有元素相加，找出最小和最大元素。
#
# 然而，cumsum()函数就不那么明显了。它将像sum()这样的每个元素相加，但是它首先将第一个元素和第二个元素相加，并将计算结果存储在一个列表中，然后将该结果添加到第三个元素中，然后再将该结果存储在一个列表中。
# 这将对数组中的所有元素执行此操作，并返回作为列表的数组之和的运行总数。


print()
print('#索引进阶')

#花式索引
# 花式索引 是获取数组中我们想要的特定元素的有效方法。

# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a) # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b) # >>>[10 50 90]
# 正如你在上面的示例中所看到的，我们使用我们想要检索的特定索引序列对数组进行索引。这反过来返回我们索引的元素的列表。


#布尔屏蔽
# 布尔屏蔽是一个有用的功能，它允许我们根据我们指定的条件检索数组中的元素。

import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
print(a)
b = np.sin(a)#对矩阵a中每个元素取正弦
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

# 上面的示例显示了如何进行布尔屏蔽。你所要做的就是将数组传递给涉及数组的条件，它将为你提供一个值的数组，为该条件返回true。

print()
print('#缺省索引')
# 不完全索引是从多维数组的第一个维度获取索引或切片的一种方便方法。
# 例如，如果数组a=[1，2，3，4，5]，[6，7，8，9，10]，那么[3]将在数组的第一个维度中给出索引为3的元素，这里是值4。

# Incomplete Indexing
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]
print(b) # >>>[ 0 10 20 30 40]
print(c) # >>>[50 60 70 80 90]

print()
print('#Where 函数')
# where() 函数是另外一个根据条件返回数组中的值的有效方法。只需要把条件传递给它，它就会返回一个使得条件为真的元素的列表。

# Where
a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b) # >>>(array([0, 1, 2, 3, 4]),)
print(c) # >>>[5 6 7 8 9]