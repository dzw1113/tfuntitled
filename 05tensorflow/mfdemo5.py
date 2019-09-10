
import  tensorflow as tf;
#神经网络：y = Wx; W=参数，x输入值，y=预测值
#激励函数：y=AF(Wx),激励函数=activation function(AF),
# 激活函数可以引入非线性因素，解决线性模型所不能解决的问题
#假设：看一只猫的图片，着重点看猫的眼睛，则提高了眼睛的值，则眼睛就被激活了。通常来说：让某一部分的神经元激活起来，传递到后面的神经元

#常有的activtion function有
#http://wiki.jikexueyuan.com/project/tensorflow-zh/api_docs/python/nn.html
'''
tf.nn.relu(features, name=None) # relu函数是目前用的最多也是最受欢迎的激活函数。
tf.nn.relu6(features, name=None) # 升级版
tf.nn.softplus(features, name=None) # softplus函数可以看作是relu函数的平滑版本
tf.nn.dropout(x, keep_prob, noise_shape=None, seed=None, name=None)
tf.nn.bias_add(value, bias, name=None)
tf.sigmoid(x, name=None)
tf.tanh(x, name=None)
'''
