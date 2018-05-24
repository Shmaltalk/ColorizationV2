from glob import glob
from os import rename
from os.path import basename

folder = '/home/taliem/ColorData/recolors/fixedPriors/'

for f in glob(folder + '*'):
#    print(basename(f))
    if basename(f).startswith('rc'):
        rename(f, folder+basename(f)[2:])
