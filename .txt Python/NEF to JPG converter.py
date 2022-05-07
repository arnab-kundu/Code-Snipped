#!pip install rawpy

import os
import rawpy
import imageio
# All files and directories ending with .txt and that don't begin with a dot:
#a=(glob.glob("D:\\NEF-files\\*.NEF")) 
#a=(glob.glob("/content/*.NEF")) 
#a=os.listdir("/content")
a=os.listdir("D:\\NEF-files")

for i in a:
    print(i)
    if i.endswith('.NEF'):
        with rawpy.imread("D:\\NEF-files\\"+i) as raw:
            rgb = raw.postprocess()
        imageio.imsave(i.replace('NEF','jpg'), rgb)
    #os.remove(i)