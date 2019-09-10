
'''
sklearn model属性

数据集地址
http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets
'''
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

#线性方程:y=kx+n
print(model.predict(data_X[:4, :]))#
print(model.coef_)#输出x的参数
print(model.intercept_)#输出跟y轴交点的坐标
print(model.get_params())#拿出定义的参数
print(model.score(data_X, data_y)) # R^2 coefficient of determination , data_X做预测值，data_y做真实值，吻合度打分操作