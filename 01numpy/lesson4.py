print('#Python、Numpy 教程:https://www.numpy.org.cn/article/basics/python_numpy_tutorial.html')

# Python是一种高级动态类型的多范式编程语言。Python代码通常被称为可运行的伪代码，因为它允许你在非常少的代码行中表达非常强大的想法，同时具有非常可读性。作为示例，这里是Python中经典快速排序算法的实现：
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

#Python 的版本

#基本数据类型
# 与大多数语言一样，Python有许多基本类型，包括整数，浮点数，布尔值和字符串。这些数据类型的行为方式与其他编程语言相似。

# Numbers(数字类型)：代表的是整数和浮点数，它原理与其他语言相同：

x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"

# 注意，与许多语言不同，Python没有一元增量(x+)或递减(x-)运算符。

# Python还有用于复数的内置类型；你可以在这篇文档中找到所有的详细信息。
# https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex