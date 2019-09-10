import tensorflow as tf
import numpy as np

# 生产模拟数据，一个一维长度为100的诉诸
x_data = np.random.rand(100).astype(np.float32);
y_data = x_data * 1.0 + 0.3

# 创建tensorflow数据结构 start
# tf.random_uniform([1],-1,1.0)：定义参数变量，由随机生产的-1到1.0
Weight = tf.Variable(tf.random_uniform([1], -1, 1.0))
# 定义初始值为0，需要一步一步的把初始值训练提升接近到1
biases = tf.Variable(tf.zeros([1]))

y = Weight * x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
#创建一个优化器，减小每次产生的误差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#初始化变量
init = tf.initialize_all_variables();
# 创建tensorflow数据结构 end


sess = tf.Session();
sess.run(init); #激活神经网络

#训练两百次
for step in range(201):
    #开始训练
    sess.run(train)
    #每20次看一下训练结果
    if step % 20 == 0:
        print(step,sess.run(Weight),sess.run(biases))

