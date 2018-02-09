#!/usr/bin/env python

from PIL import Image as im 
import os
from resizeimage import resizeimage
import numpy as np
def resize(input, output, row, col):
    with open(input, 'r+b') as f:
        with im.open(f) as image:
            print("I'm at ", input)
            cover = image.resize((row, col))
            cover.save(output, image.format)




rootdir = "data"
row=0
col=0
count = 0 

#first find the average dimensions
for subdir, dirs, files in os.walk(rootdir):
    for subdir, dirs, files in os.walk(subdir):
        if(len(files)):
            for image in files:
                
                pic = np.array(im.open(subdir+"/"+image))
                count = count+1
                row = row + pic.shape[0]
                col = col + pic.shape[1]


row = row/count
col = col/count
     
# resize!
for subdir, dirs, files in os.walk(rootdir):
    for subdir, dirs, files in os.walk(subdir):
        if(len(files)):
            for image in files:
                resize(subdir+"/"+image, subdir+"/"+image, col, row)

