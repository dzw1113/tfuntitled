import numpy as np

print("理解 NumPy:https://www.numpy.org.cn/article/basics/understanding_numpy.html")

print('定义数组')
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)

print()

print('包含5个元素的数组,称之为形状,分别打印对应索引的值')
print(my_array.shape)

print(my_array[0])
print(my_array[1])

print('重新赋值')
my_array[0]=-1
print(my_array)

print()

print('创建一个长度为5的NumPy数组，但所有元素都为0')
my_new_array = np.zeros((5))
print(my_new_array)

print('创建一个长度为5的NumPy随机值数组')
my_random_array = np.random.random((5))
print(my_random_array)

print('创建二维数组,(2, 3) 分别表示2行，3列,多维数组可以用 my_array[i][j] 符号来索引，其中i表示行号，j表示列号。i和j都从0开始')
my_2d_array = np.zeros((2, 3))
print(my_2d_array)
my_2d_array = np.ones((2, 3))
print(my_2d_array)

print()
print('代码片段的输出是5，因为它是索引0行和索引1列中的元素。')
my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])
print(my_array.shape)

print('假设，我们想从中提取第二列（索引1）的所有元素。在这里，我们肉眼可以看出，第二列由两个元素组成：5 和 1.冒号(:)代表列，列号值为1')
my_array_column_2 = my_array[:, 1]
print(my_array_column_2)

print()
print('实战')
print()


import numpy as np
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum = \n", sum )
print("Difference = \n", difference )
print("Product = \n", product )
print("Quotient = \n", quotient )


#输出结果
# Sum = [[ 6. 8.] [10. 12.]]
# Difference = [[-4. -4.] [-4. -4.]]
# Product = [[ 5. 12.] [21. 32.]]
# Quotient = [[0.2 0.33333333] [0.42857143 0.5 ]]

print()
print('如你所见，乘法运算符执行逐元素乘法而不是矩阵乘法。 要执行矩阵乘法，你可以执行以下操作')

matrix_product = a.dot(b)
print("Matrix Product = ", matrix_product)

