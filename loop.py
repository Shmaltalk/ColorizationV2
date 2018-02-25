import subprocess


lists_f = open('data/smallTest.txt', 'r')
containing_path = './testimages/'
#containing_path = '/home/taliem/ColorData/flowers/64x64/'

for img in lists_f:
    img = img.strip()
    full_path = containing_path + img
    subprocess.call(['python3','demo.py', full_path])

#for f in glob.glob('testimages/*'):
#    subprocess.call(['python3', 'demo.py', f])
