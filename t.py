from __future__ import print_function
import tensorflow as tf
hello = tf.constant("Hello, World of AI")
sess = tf.Session()
print(sess.run(hello))

Output: "Hello, World of AI!"
