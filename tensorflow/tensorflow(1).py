import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")

sess = tf.Session()

print(sess.run(hello))

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b
#
# print(sess.run(a))