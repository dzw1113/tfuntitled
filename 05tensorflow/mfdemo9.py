# 定义一个神经网络：输入层（一个），隐藏层（十个）和输出层（一个）

import tensorflow as tf;
import numpy as np;
import matplotlib.pyplot as plt;#可视化模块


def add_layer(inputs, in_size, out_size, activation_function=None):
    # tf.random_normal([in_size, out_size])生成一个随机数的矩阵变量,
    Weights = tf.Variable(tf.random_normal([in_size, out_size]));
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1);
    # 矩阵乘法：tf.matmu
    Wx_plus_b = tf.matmul(inputs, Weights) + biases;
    if activation_function is None:
        outputs = Wx_plus_b;
    else:
        outputs = activation_function(Wx_plus_b);
    return outputs;


xs = tf.placeholder(tf.float32, [None, 1],name='x_input');
ys = tf.placeholder(tf.float32, [None, 1],name='y_input');

# 定义数据形式
# linspace:在指定的间隔内返回均匀间隔的数字。
# [:, np.newaxis]; 把 [1,2]一维数组转换成[[1],[2]]二维数组
x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis];
noise = np.random.normal(0, 0.05, x_data.shape);
y_data = np.square(x_data) - 0.05 + noise;

# 定义隐藏层,
l1 = add_layer(x_data, 1, 10, activation_function=tf.nn.relu)
# 定义输出层
predition = add_layer(l1, 10, 1, activation_function=None);

# 预测值
# reduce_sum = 求和
# square = 计算平方
# reduce_mean = 平均值
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition), reduction_indices=[1]))

# 学习的效率要小与1,梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss);

# 初始化所有变量
init = tf.initialize_all_variables();

#生成一个图片框，想做一个连续性的画图
fig = plt.figure();
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
#show不影响主线程运行
plt.ion()
plt.show();

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        feed_dict = {xs: x_data, ys: y_data};
        sess.run(train_step, feed_dict=feed_dict)
        if i % 50 == 0:
            try:
                # 在图片里去除lines的第一个线段
                ax.lines.remove(lines[0]);
            except:
                pass;
            predition_value = sess.run(predition,feed_dict=feed_dict);
            #线为红色，宽度为5
            lines = ax.plot(x_data,predition_value,'r-',lw=5)

            #暂停0.1秒
            plt.pause(0.1)
