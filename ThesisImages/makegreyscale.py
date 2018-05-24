from glob import glob
from skimage.color import rgb2grey, grey2rgb
from skimage.io import imread, imsave
from os.path import basename
import numpy as np


folder = '/home/taliem/ColorData/recolors/testimages128/'
out_folder = '/home/taliem/ColorData/recolors/bw128/'

for f in glob(folder+'*'):
    img = imread(f)
    img = grey2rgb(rgb2grey(np.copy(img)))
#    print(np.shape(img))
    imsave(out_folder+basename(f), img)
