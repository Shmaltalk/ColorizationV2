import subprocess

lists_f = open('/home/taliem/color-redo/colorization-tf/data/smallTest.txt', 'r')
original_path = '/home/taliem/ColorData/flowers/64x64/'
recolor_path = '/home/taliem/ColorData/recolors/photoshop64to4/'

for img in lists_f:
    img = img.strip()
    full_original = original_path + img
    full_recolor = recolor_path + img
    subprocess.call(['c1', 'python', 'get_metrics_two.py', original_path, recolor_path])
