import os, sys
from skimage.color import rgb2yuv
from skimage.io import imsave
# header
# filename, model_number, uncompressed_size, jpeg_size, current_size, jpeg_compression, current_compression,
# (image1) PSNR SSIM MSSSIM VIFP PSNRHVS PSNRHVSM
# (image2) PSNR SSIM MSSSIM VIFP PSNRHVS PSNRHVSM

original_path = '/home/taliem/ColorData/flowers/64x64/'
recolor_path = '/home/taliem/ColorData/recolors/128from128training-350000/'
stats = {'psnr': 0, 'ssim': 0, 'vifp': 0, 'psnrhvs': 0, 'psnrhvsm': 0}



def get_metrics(first, second):
    
    metrics = "PSNR SSIM VIFP PSNRHVS PSNRHVSM".lower().split(' ')
    size = [64, 64]
    # first convert both the  images to yuv format
    size_x = size[0] - size[0]%16 # this is to make sure we can get MS-SSIM 
    size_y = size[1] - size[1]%16 # metrics from VQMT, which requires divisible by 16

    for x in [first, second]:
        yuv_convert_command = "ffmpeg -hide_banner -loglevel panic -y -i " + x +" -s " + str(size_x) + "x" + str(size_y) + " -pix_fmt yuv420p " + x +".yuv"
#        print yuv_convert_command
        if os.system(yuv_convert_command) != 0:
            raise Exception("FFMPEG was not found")
        # print command
        
    for img_com in [second]:
        command_metrics = "/home/taliem/vqmt " + \
                          first+".yuv " + \
                          second+".yuv " + \
                          str(size_x) + " " + \
                          str(size_y) + " " + \
                          "1 1 out PSNR SSIM VIFP PSNRHVS PSNRHVSM"
        if os.system(command_metrics) != 0:
            raise Exception("VQMT was not found, please install it from https://github.com/Rolinh/VQMT")
        for m in metrics:
            f = open('out_' + m + '.csv').read().splitlines()[1].split(',')[1]
            print f,
            stats[m] += float(f)
        print ''
            
    print stats
    

if __name__=='__main__':
    strng = "yellowapple.png"
    print(strng)
    get_metrics("./" + strng, "./greenapple.png")
#    num_images = 0
#    lists_f = open('/home/taliem/color-redo/colorization-tf/data/test.txt', 'r')
#
#    for img in lists_f:
#        num_images += 1
#        img = img.strip()
#        get_metrics(original_path + img, recolor_path + img)
#    print num_images


