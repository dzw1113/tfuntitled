'''
https://github.com/MorvanZhou/tutorials/tree/master/sklearnTUT


https://www.jianshu.com/p/cd5a929bec33

Sklearn 包含了很多种机器学习的方式:

Classification 分类
Regression 回归
Clustering 非监督分类
Dimensionality reduction 数据降维
Model Selection 模型选择
Preprocessing 数据预处理


'''

'''
Classification 分类
http://blog.csdn.net/yuanyu5237/article/details/44278759
'''

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#加载花瓣数据集
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# print(iris_X[:2, :])
# print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=0.3)

##print(y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train);#利用模型去学习训练
print(knn.predict(X_test));#输出训练出后的数据
print(y_test);#输出真实数据