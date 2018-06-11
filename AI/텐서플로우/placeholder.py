import tensorflow as tf

#a = tf.placeholder(tf.int32, [3])
a = tf.placeholder(tf.int32, [None]) # 숫자 갯수 정해주지 않아도 가능.
#b = tf.constant(2)
b = tf.constant(10)
#x2_op = a*b
x10_op = a/b

sess = tf.Session()

#r1 = sess.run(x2_op, feed_dict = {a:[1,2,3]})
r1 = sess.run(x10_op, feed_dict = {a:[1,2,3,4,5]})
print(r1)
#r2 = sess.run(x2_op, feed_dict = {a:[10,20,10]})
r2 = sess.run(x10_op, feed_dict = {a:[10,20]})
print(r2)