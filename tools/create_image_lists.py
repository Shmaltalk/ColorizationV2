import os
'''
    Call this only from the main folder.
'''

f = open('data/train.txt', 'w')
basepath = './flowers/'
truepath = '/home/taliem/ColorData/flowers/64x64/'
for p1 in os.listdir(basepath):
    #image = os.path.abspath(basepath + p1)
    path = truepath + p1
    f.write(path + '\n')
f.close()

g = open('data/test.txt', 'w')
basepath = './testimages/'
for p in os.listdir(basepath):
    #image = os.path.abspath(basepath + p)
    g.write(p + '\n')
g.close()
