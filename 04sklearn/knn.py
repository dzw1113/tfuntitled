'''
http://blog.csdn.net/wstz_5461/article/details/78018099

KNN：k-Nearest Neighbors，临近算法

假设绿色的圆是农场里的鹰，蓝色正方形是附近的老鹰，红色三角形是农场里的鸡，农场里的鹰会认为自己是鹰还是鸡，取决于它自己心里的“K”，如果K是3，那么它会认为自己是鸡，如果K是5那么它会认为自己是鹰。
可见环境的影响是多么重要，而且我们也应该开阔自己的视野，让自己成为一只老鹰而不是农场里的一只鸡


scikit-learn K最近邻分类器 KNeighborsClassifier 使用
http://blog.csdn.net/hjh00/article/details/63808075
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

feature_names = [
    'area',
    'perimeter',
    'compactness',
    'length of kernel',
    'width of kernel',
    'asymmetry coefficien',
    'length of kernel groove',
]

COLOUR_FIGURE = False


def plot_decision(features, labels, num_neighbors=3):
    y_min, y_max = features[:, 2].min() * .9, features[:, 2].max() * 1.1
    x_min, x_max = features[:, 0].min() * .9, features[:, 0].max() * 1.1
    X, Y = np.meshgrid(np.linspace(x_min, x_max, 1000), np.linspace(y_min, y_max, 1000))

    model = KNeighborsClassifier(num_neighbors)
    model.fit(features[:, (0, 2)], labels)
    C = model.predict(np.vstack([X.ravel(), Y.ravel()]).T).reshape(X.shape)
    if COLOUR_FIGURE:
        cmap = ListedColormap([(1., .7, .7), (.7, 1., .7), (.7, .7, 1.)])
    else:
        cmap = ListedColormap([(1., 1., 1.), (.2, .2, .2), (.6, .6, .6)])
    fig, ax = plt.subplots()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel(feature_names[0])
    ax.set_ylabel(feature_names[2])
    ax.pcolormesh(X, Y, C, cmap=cmap)
    if COLOUR_FIGURE:
        cmap = ListedColormap([(1., .0, .0), (.1, .6, .1), (.0, .0, 1.)])
        ax.scatter(features[:, 0], features[:, 2], c=labels, cmap=cmap)
    else:
        for lab, ma in zip(range(3), "Do^"):
            ax.plot(features[labels == lab, 0],
                    features[labels == lab, 2],
                    ma,
                    c=(1., 1., 1.),
                    ms=6)
    return fig, ax


def load_csv_data(filename):
    data = []
    labels = []
    datafile = open(filename)
    for line in datafile:
        fields = line.strip().split('\t')
        data.append([float(field) for field in fields[:-1]])
        labels.append(fields[-1])
    data = np.array(data)
    labels = np.array(labels)
    return data, labels


def accuracy(test_labels, pred_lables):
    correct = np.sum(test_labels == pred_lables)
    n = len(test_labels)
    return float(correct) / n


if __name__ == '__main__':
    features, labels = load_csv_data('knn.csv')
    print(labels)