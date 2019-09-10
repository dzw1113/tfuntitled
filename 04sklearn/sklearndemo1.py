
'''
sklearn dataset数据集

数据集地址
http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets
'''

from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

#http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston
#波士顿房价案例，506个样本数据，13个属性
print(loaded_data.data.shape)

#利用线性回归模式训练数据
model = LinearRegression()
model.fit(data_X, data_y);#利用模型去学习

print(model.predict(data_X[:4, :]));#输出训练后的四个值
print(data_y[:4])#输出真实值

X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)#创造数据，生成一百个样本
plt.scatter(X, y)#生成散点图
plt.show()