import tensorflow as tf
from utils import *
from net import Net
from skimage.io import imsave
from skimage.transform import resize
import skimage.color
import cv2
import os.path
import utils
import numpy as np


#print(sys.argv[1])

def test(imgname, sess):
  
  #output_dir = '/home/taliem/color-redo/'
  output_dir = '/home/taliem/ColorData/recolors/thumbnail2/'

  img = cv2.imread(imgname)
#  print(img.shape)
  
  data_input, original_ab, prior_boost_nongray = utils.preprocess(np.copy(img[None, :, :, :]))
  data_input = data_input.astype(dtype=np.float32)
 # print(type(data_input))
  
  #only the L channel
  data_l = (cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)).astype(dtype=np.float32)
  #print("original", data_l.shape)
  data_l = data_l[None, :, :, None] / 255.0 * 100 - 50
#  print("max, min", data_l.max(), data_l.min())
#  print(data_l.shape)\

     
  #conv8_313 = autocolor.inference(data_input)

  output = sess.run(conv8_313, feed_dict={conv_placeholder:data_input})

    
#  print("min, max, shape", data_l.min(), data_l.max(), data_l.shape)
  img_rgb = decode(data_l, output, 2.63)
  stack = np.hstack((img_rgb, img[:,:,::-1].astype(dtype=np.float32) / 255.0))
  #  print(img_rgb.shape)
  new_name = output_dir + os.path.basename(imgname)
  #imsave(img_rgb)
  imsave(new_name, stack)


if __name__ == "__main__":
  lists_f = open('data/test.txt', 'r')
  containing_path = '/home/taliem/ColorData/flowers/64x64/'
  model = '/home/taliem/ColorData/models/thumbnail2.ckpt'

  autocolor = Net(train=False)
  conv_placeholder = tf.placeholder(tf.float32, (1, 64, 64, 3))
  conv8_313 = autocolor.inference(conv_placeholder)
  
  saver = tf.train.Saver()
  with tf.Session() as sess:
    saver.restore(sess, model)
    for img in lists_f:
      img = img.strip()
      full_path = containing_path + img
      test(full_path, sess)
  
  
 # for img in lists_f:
 #   img = img.strip()
 #   full_path = containing_path + img
 #   test(full_path, first)
 #   first = False
