
#分类可以生成多个值
import tensorflow.compat.v1 as tf
import numpy as np
from tensorflow_core.examples.tutorials.mnist import input_data
tf.disable_eager_execution()

#1 to 10 data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

def add_layer(inputs, in_size, out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    bias = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + bias

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs


def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs}) # 1 * 10
    #对比预测是否正确
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1)) #tf.argmax 记录每一行、列的最大值索引 0：列 1：行  tf.equal: 判断是否相等-》bool
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result

#define placeholder for inputs to network
xs = tf.placeholder(tf.float32,[None,784])
ys = tf.placeholder(tf.float32,[None,10])

#add output layer
prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax) # nn.softmax常用于classificaiton

#the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))# loss
# reduction_indices=[1] 表示处理维度

train_step = tf.train.GradientDescentOptimizer(0.5).minimize((cross_entropy))

sess= tf.Session()
sess.run(tf.initialize_all_variables())

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100) #提取100个数据
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})

    if i % 50 == 0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))