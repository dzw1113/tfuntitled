import numpy as np

print("索引与切片:https://www.numpy.org.cn/user_guide/numpy_basics/indexing.html")

print('数组基础')

x = np.arange(10)

print('#单个元素索引:一维数组的单元素索引是人们所期望的。它的工作方式与其他标准Python序列完全相同。它是从0开始的，并且接受负索引来从数组的结尾进行索引。')
print(x[2])
print(x[-2])

print('与列表和元组不同，numpy数组支持多维数组的多维索引。这意味着没有必要将每个维度的索引分成它自己的一组方括号。')

print('x的最大值是10，形状为5*2二维数组')
x.shape = (5,2)
print(x)

print('x的最大值是10，形状为2*5二维数组')
x.shape = (2,5) # now x is 2-dimensional
print(x)
print(x[0,3])
print(x[1,3])

print(x[1,-1])

print('请注意，如果索引索引数量少于维度的多维数组，则会得到一个子维数组。例如：')

print(x[0])
print(x[0][1])

print('因此，请注意，x [0,2] = x [0] [2]， 但是第二种情况效率更低，因为一个新的临时数组在第一个索引后创建了，这个临时数组随后才被2这个数字索引。'
      '请注意那些用于IDL或Fortran内存顺序的索引。Numpy使用C顺序索引。这意味着最后一个索引通常代表了最快速变化的内存位置，与Fortran或IDL不同，第一个索引代表内存中变化最快的位置。'
      '这种差异代表着很大的混乱的可能性。')


print('#其他索引选项')

x = np.arange(10)
print(x[2:5]) #从索引2-5

print('取-10至-1的数据')
print(x[:-1])
print('取前1个数据')
print(x[:1])

print(x[1:])
print(x)

print()

y = np.arange(35).reshape(5,7)
print(y)
print()
print(y[1:5:2,::3])#难以理解

print()
print('#索引数组')

x = np.arange(10,1,-1)

print(x)
print('索引数组必须是整数类型。数组中的每个值指示数组中要使用哪个值来代替索引')
print(x[np.array([3, 3, 1, 8])])

print(x[np.array([3,3,-3,8])])

print('一般来说，使用索引数组时返回的是与索引数组具有相同形状的数组，但是索引数组的类型和值。')

print(x[np.array([[1,1],[2,3]])])

print('#索引多维数组')

print('在这种情况下，如果索引数组具有匹配的形状，并且索引数组的每个维都有一个索引数组，则结果数组具有与索引数组相同的形状，并且这些值对应于每个索引集的索引在索引数组中的位置。在此示例中，两个索引数组的第一个索引值为0，因此结果数组的第一个值为y [0,0]。下一个值是y [2,1]，最后一个是y [4,2]。')


print(y[np.array([0,2,4]), np.array([0,1,2])])
print(y[4,2])

print('广播机制允许索引数组与其他索引的标量组合。结果是标量值用于索引数组的所有对应值：')
print(y[np.array([0,2,4]), 1])

print('索引数组的每个值从被索引的数组中选择一行，并且结果数组具有结果形状（行的大小，数字索引元素）,这可能有用的一个示例是用于颜色查找表，我们想要将图像的值映射到RGB三元组中进行显示。')
print(y[np.array([0,2,4])])

print('#布尔值或掩码索引数组')

b = y>20
print(y[b])
print(b[:,5])

print(y[b[:,5]])

# 例如，使用具有四个真实元素的形状（2,3）的二维布尔阵列来从三维形状（2,3,5）阵列中选择行会得到形状的二维结果（4 ，5）：
x = np.arange(30).reshape(2,3,5)
print(x)

b = np.array([[True, True, False], [False, True, True]])
print(b)
print(x[b])


print()
print()
print('#组合索引和切片')

print(y)
print(y[np.array([0,2,4]),1:3])


print('#结构化索引工具')
# 为了便于将数组形状与表达式和赋值相匹配，可以在数组索引中使用np.newaxis对象来添加大小为1的新维度。例如：
print(y.shape)
print(y[:,np.newaxis,:].shape)
# 请注意，数组中没有新元素，只是增加了维度。这可以很方便地以一种其他方式需要明确重塑操作的方式组合两个数组。例如：

x = np.arange(5)
print(x[:,np.newaxis] + x[np.newaxis,:])

print()
# 省略号语法可以用于指示完整地选择任何剩余的未指定的维度。例如：
z = np.arange(81).reshape(3,3,3,3)
print(z)
print(z[1,...,2])