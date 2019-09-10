import input_data
# mnist是一个以numpy数组形式存储训练、验证和测试数据的轻量级类
mnist = input_data.read_data_sets('MNIST_data', one_hot=True, source_url='http://yann.lecun.com/exdb/mnist/')

import tensorflow as tf

#构建计算图
sess = tf.InteractiveSession();

#tf.placeholder：用于得到传递进来的真实的训练样本：
#不必指定初始值，可在运行时，通过 Session.run 的函数的 feed_dict 参数指定；
#这也是其命名的原因所在，仅仅作为一种占位符；
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))