import numpy as np

print("python切片:https://www.cnblogs.com/yanwuliu/p/9567466.html")

# 1、列表list中使用

print('1、range()生成器')
l=list(range(10))
print(l)

l=list(range(1,11))
l=['a','b','c','d','e','j','k','l','m','n','o']
print(l)

# 切片操作的特点：
#
# 顾头不顾尾
# 使用range()生成器时，如果冒号前面没写的话，代表从0开始取元素
# 使用range()生成器时，如果冒号后面没写的话，代表取到最后的元素
# 如果冒号前后都没写的话，代表取全部

print(l[2:8])#顾头不顾尾
print(l[:5])#如果冒号前面没写的话，代表从0开始取的
print(l[4:])#如果冒号后面没写的话，代表取到最后
print(l[:])#如果冒号前后都没写的话，代表取全部


print()
print('2、 步长')
# 步长特点：
#
# 如果步长是正数的话，就从前往后开始取值；
# 如果步长是负数的话，就从后往前开始取值，类似于reverse()。

nums=list(range(1,11))
print(nums)
print(nums[1::2])#打印偶数
#1 2 3 4 5 6 ...10
print(nums[::2])#打印奇数
print(nums[::-2]) #取偶数，从右往左取值


print()
print()
# 2、字符串中使用
words='中秋节要上课'
print(words[0])
print(words[::-1])
print(words[::-2])