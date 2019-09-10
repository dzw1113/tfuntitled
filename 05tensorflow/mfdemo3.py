import tensorflow as tf;

#tf中的Variable运用

#变量
state = tf.Variable(0,name='counter');

#常量
one = tf.constant(1);

#两个相加
new_value = tf.add(state,one)
#把new_value指向更新到state
update = tf.assign(state,new_value)

#初始化所有变量，如果有定义变量的情况下
init = tf.initialize_all_variables();

with tf.Session() as sess:
    sess.run(init);
    for _ in range(3):
        sess.run(update);
        print(sess.run(state))