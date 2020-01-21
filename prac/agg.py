import tensorflow as tf
import numpy as np

shape = [height, width, channels]
x = tf.placeholder(dtype = tf.float32, shape = shape)
rot_90 = tf.image.rot90('/home/harish/Desktop/videosforabg/dog1.jpg', k=1)
rot_180 = tf.image.rot90('/home/harish/Desktop/videosforabg/dog1.jpg', k=2)
# To rotate in any angle. In the example below, 'angles' is in radians
shape = [batch, height, width, 3]
y = tf.placeholder(dtype = tf.float32, shape = shape)
rot_tf_180 = tf.contrib.image.rotate(y, angles=3.1415)
# Scikit-Image. 'angle' = Degrees. 'img' = Input Image
# For details about 'mode', checkout the interpolation section below.
rot = skimage.transform.rotate('/home/harish/Desktop/videosforabg/outputdog1.jpg', angle=45, mode='reflect')


