import tensorflow as tf;

#学习tf会话控制简单运用


martrix1 = tf.constant([[3,3]]);
martrix2 = tf.constant([[2],[2]]);

#tf里的矩阵用tf.dot(m1,m2)
product = tf.matmul(martrix1,martrix2)

# 方法1
sess = tf.Session();
result = sess.run(product)
print(result)
sess.close()


# 方法2
with tf.Session() as sess1:
    result2 = sess1.run(product);
    print(result2)