import tensorflow as tf
from utils import *
from net import Net
from skimage.io import imsave
from skimage.transform import resize
import skimage.color
import cv2
import sys
import os.path
import utils
import numpy as np





#print(sys.argv[1])
img = cv2.imread(sys.argv[1])


model = '/home/taliem/ColorData/models/thumbnail64to4px-ImgNetPriors.ckpt'
#output_dir = '/home/taliem/color-redo/'
output_dir = '/home/taliem/ColorData/recolors/thumbnail64to4px-ImgNetPriors/'

print(img.shape)

data_input, original_ab, prior_boost_nongray = utils.preprocess(np.copy(img[None, :, :, :]))
data_input = data_input.astype(dtype=np.float32)


#only the L channel
data_l = (cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)).astype(dtype=np.float32)
#print("original", data_l.shape)
data_l = data_l[None, :, :, None] / 255.0 * 100 - 50
print("max, min", data_l.max(), data_l.min())
print(data_l.shape)



#img = img[None, :, :, :]
#print(img.shape)
#data_input = skimage.color.rgb2lab(np.copy(img))
#data_input = data_input.astype(dtype=np.float32)
#data_input[:, :, :, 1:] = downsample_color_channels(img)[:, :, :, 1:]
#data_input = data_input[:, :, :, 0] - 50

#data_l = tf.placeholder(tf.float32, shape=(None, None, None, 1))
autocolor = Net(train=False)

conv8_313 = autocolor.inference(data_input)

saver = tf.train.Saver()
with tf.Session() as sess:
  saver.restore(sess, model)
  conv8_313 = sess.run(conv8_313)

#test
#img_rgb = np.concatenate(data_l, original_ab)
#print(img_rgb.shape)q
#img_rgb[:, :, :, 0] = data_l
#img_rgb[:, :, :, 1:] = original_ab

print("min, max, shape", data_l.min(), data_l.max(), data_l.shape)
img_rgb = decode(data_l, conv8_313, 2.63)
print(img_rgb.shape)
new_name = output_dir + '3' + os.path.basename(sys.argv[1])
imsave(new_name, img_rgb)
