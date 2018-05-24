from skimage.io import imsave,imread
import numpy as np


input_file = '/home/taliem/color-redo/colorization-tf/data/test.txt'
lists_f = open(input_file, 'r').readlines()

bw = '/home/taliem/ColorData/recolors/bw/'
color = '/home/taliem/ColorData/recolors/64from64training/'

stack = None

i = 1

for img in lists_f:
    img = img.strip()
    bw_image = np.copy(imread(bw+img))
    color_image = np.copy(imread(color+img))
    
    row = np.hstack((bw_image, color_image))
    if stack is None:
        stack = row
    else:
        stack = np.vstack((stack, row))
    
    if i%15 == 0:
        imsave('/home/taliem/color-redo/thesis-images/appendix'+ str(i//15) +'.png', stack)
        stack = None

    i+=1
print(i)
