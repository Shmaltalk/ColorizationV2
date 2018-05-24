from skimage.io import imsave
import numpy as np
import cv2

output_name = '/home/taliem/color-redo/thesis-images/thumbnail-diffPriors.jpg'

row_1 = '/home/taliem/ColorData/flowers/64x64/'
row_bw = '/home/taliem/ColorData/recolors/photoshop64to4/'
#row_2 = '/home/taliem/ColorData/recolors/thumbnail1/'
#row_3 = '/home/taliem/ColorData/recolors/thumbnail2-only/'
row_4 = '/home/taliem/ColorData/recolors/thumbnail-noPriors-only/'
row_5 = '/home/taliem/ColorData/recolors/thumbnail-flowerPriors-only/'


#imgs = ['ocean.jpg', 'gray.jpg', 'Yosemite.jpg', 'fire.jpg']
imgs = ['image_00029.jpg', 'image_02109.jpg', 'image_03269.jpg', 'image_07109.jpg', 'image_02189.jpg', 'image_00909.jpg', 'image_05869.jpg', 'image_06429.jpg', 'image_01789.jpg']

r1_img = np.copy(cv2.imread(row_1 + imgs[0]))[:, :, ::-1]
bw_img = np.copy(cv2.imread(row_bw + imgs[0]))[:, :, ::-1]
#r2_img = np.copy(cv2.imread(row_2 + imgs[0]))[:, :, ::-1]
#r3_img = np.copy(cv2.imread(row_3 + imgs[0]))[:, :, ::-1]
r4_img = np.copy(cv2.imread(row_4 + imgs[0]))[:, :, ::-1]
r5_img = np.copy(cv2.imread(row_5 + imgs[0]))[:, :, ::-1]

imgs = imgs[1:]
#print(imgs)

for img in imgs:
    temp_1 = np.copy(cv2.imread(row_1+img))[:, :, ::-1] #in RGB
    temp_bw = np.copy(cv2.imread(row_bw+img))[:, :, ::-1] #in RGB
#    temp_2 = np.copy(cv2.imread(row_2+img))[:, :, ::-1] #in RGB
#    temp_3 = np.copy(cv2.imread(row_3+img))[:, :, ::-1] #in RGB
    temp_4 = np.copy(cv2.imread(row_4+img))[:, :, ::-1] #in RGB
    temp_5 = np.copy(cv2.imread(row_5+img))[:, :, ::-1] #in RGB

    r1_img = np.hstack((r1_img, temp_1))
    bw_img = np.hstack((bw_img, temp_bw))
#    r2_img = np.hstack((r2_img, temp_2))
#    r3_img = np.hstack((r3_img, temp_3))
    r4_img = np.hstack((r4_img, temp_4))
    r5_img = np.hstack((r5_img, temp_5))


#print(np.sum(r4_img), np.sum(r5_img), np.sum(r2_img))
stack = np.vstack((r1_img, bw_img))
#stack = np.vstack((stack, r2_img))
#stack = np.vstack((stack, r3_img))
stack = np.vstack((stack, r4_img))
stack = np.vstack((stack, r5_img))


imsave(output_name, stack)
