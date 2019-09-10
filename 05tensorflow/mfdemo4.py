import tensorflow as tf;

#tf 中placeholder当作入参运用

#定义入参类型，值未知
input1 = tf.placeholder(tf.float32);
input2 = tf.placeholder(tf.float32);

#相乘
ouput = tf.multiply(input1,input2);

with tf.Session() as sess:
    #定义字典，告诉input1为7.0，input2为2.0
    fee_dict = {input1: [7.], input2: [2.]};
    print(sess.run(ouput,fee_dict));

