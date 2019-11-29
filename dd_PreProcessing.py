"""
dd_PreProcessing.py

Usage:
    $ python dd_PreProcessing.py 

Overview of the methods:
- Transforms the input image (color or grey scale) into a black and white image by applying a threshold'
- Divide the image into two, if it were double scanned
- Cut the picture in the middle if it is double scanned
- Extract page number and cut the area
- Separate the picture and text in two columns
- Clipping the text-part
- Determine the angle if the page was not right scanned

The threshold is chosen automatically via the otsu method.
"""

import os
import numpy as np
import sys
from scipy import linalg, ndimage, signal
from skimage.io import imread
from PIL import Image
import imageio
import glob
import pytesseract 
import os
from pytesseract import image_to_string
import re
from skimage import filters
from extract_raster_maps import *


'''
# 1. Transforms the input image (color or grey scale) 
# into a black and white image by applying a threshold
'''
def dd_transformToBW(img_path) :
    # Open the input image
    img = imread(img_path)
    # Check whether the image is in color (in that case, it is a 3 or 4D array
    # as opposed to greyscale which are 2D
    if len(img.shape) == 3:
        # Turn it to greyscale by averaging out the last dimension, i.e. the
        # channel.  If the image has some alpha value, it is simply ignored
        # here.
        img = img[:, :, :3].mean(axis=-1)
    
    # Get the threshold via the otsu method
    th = filters.threshold_otsu(img)
    # Turn to B/W: 0 for black and 255 for white
    # Each pixel with a value greater than the threshold gets white.
    bw = (img > th) * 255
    return bw

  
'''
 Divide the image into two, if it were double scanned
'''
def dd_divImage(img):
    # hight, width
    h, w = img.shape
    p1 = []
    p2 = []
    # print(h,w)
    # In case the picture is rotated
    if(w < h):
        w = h
        # img = np.rot90(img, k=1, axes=(0, 1))# left rotation
    else:
        img = np.rot90(img, k=1, axes=(1, 0))  # right rotation
    # print(h,w)
    # Check if it is white pixel line in the middle
    if (np.mean(img[int(w / 2)] > 254)):
        p1 = img[0:int(w / 2)]
        p1 = np.rot90(p1, k=1, axes=(0, 1))
        p2 = img[int(w / 2):w]
        p2 = np.rot90(p2, k=1, axes=(0, 1))
    return p1, p2 


'''
 Separate the image in cols by given axis(must be program)
'''
def dd_sepImageinBlocks(bw_img, axis=0):
    blocks = []
    if( axis == 0 ):
        bw_img = np.rot90(bw_img, k=1, axes=(0, 1))
    h,w = bw_img.shape
    startIndex = 0
    blockIndex = 0

    for x in range(h):
        # the first line with something
        if (np.mean(bw_img[x]) < 254) and startIndex == 0:
            startIndex = x
        # the end of the found block is white
        if (np.mean(bw_img[x]) >= 254) and startIndex > 0:
            # define the block
            clipBlock_Temp = bw_img[startIndex:x]
            # only if is shown in the picture#
            if(np.mean(clipBlock_Temp) < 250):
                if( axis == 0 ):
                    clipBlock_Temp = np.rot90(clipBlock_Temp, k=1, axes=(1, 0))
                blocks.append(clipBlock_Temp)
                blockIndex = blockIndex + 1
                startIndex = 0
      
    return blocks   


'''
 Thus method returns the page number. From the config file
 is checked if the numer is on top or bottom, verticalPos = 0 | 1-top | bottom
'''
def dd_getPageNumber(img):
    startIndex = 0
    endIndex = 0
    res = 0
    shareBlock = []
    h, w = img.shape
    for x in range(h):
        if (np.mean(img[x]) < 254) and startIndex == 0:
            startIndex = x
        if (np.mean(img[x]) > 254) and startIndex > 0:
            shareBlock = img[startIndex:x]
            startIndex = 3
            endIndex = x
            break
   
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    #head_text = pytesseract.image_to_string(Image.fromarray(head)).replace(' ', '')
    t = image_to_string(shareBlock)
    res = [int(i) for i in t.split() if i.isdigit()]
    img = img[endIndex:h] 
    
    return res, img    

 
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles   


'''
'''
def getCofigurations(dirName):
    fobj = open(dirName)
    configList = []
    for line in fobj:
        if(line[0] != "#"):
            splitTemp = line.split("=")
            configList.append(re.sub("\n","",splitTemp[1]))
            
    fobj.close()  
    return configList
       
   
# The usual "main" script
if __name__ == '__main__':
    # Parsing arguments, see threshold.py or extract_raster_maps.py
    configList = getCofigurations("D:/distribution_digitizer/2019/config.txt")
    
    dirNameinput = configList[0]
    dirNameoutput = configList[1]
    print(dirNameinput)
    # get the files
    #listOfFiles = [f for f in os.listdir(dirName) if re.match(r'.*\.tiff', f)]
    listOfFiles = getListOfFiles(dirNameinput)
    for file in listOfFiles:
        print(file)
        # 1.
        bw = dd_transformToBW(file)
        
        # 2.
        if(configList[2] == '2'):
            p1, p2 = dd_divImage(bw) 
            #Image.fromarray(p1.astype(np.uint8)).save(dirNameoutput+"p1.tiff")
            #Image.fromarray(p2.astype(np.uint8)).save(dirNameoutput+ "p2.tiff")
            
            # 3.
            pNumber1, p1 = dd_getPageNumber(p1)
            pNumber2, p2 = dd_getPageNumber(p2)
            
            if(os.path.isdir(dirNameoutput+"/"+ str(pNumber1[0])) == False):
                os.mkdir(dirNameoutput+"/"+ str(pNumber1[0]))
            if(os.path.isdir(dirNameoutput+"/"+ str(pNumber2[0])) == False):
                os.mkdir(dirNameoutput+"/"+ str(pNumber2[0]))
            Image.fromarray(p1.astype(np.uint8)).save(dirNameoutput + str(pNumber1[0]) +"/"+ str(pNumber1[0]) +"_orign.tiff")
            Image.fromarray(p2.astype(np.uint8)).save(dirNameoutput + str(pNumber2[0]) +"/"+ str(pNumber2[0]) +"_orign.tiff")
           
            Image.fromarray(p1.astype(np.uint8)).save(dirNameoutput + str(pNumber1[0]) +"/" + str(pNumber1) +".tiff")
            Image.fromarray(p2.astype(np.uint8)).save(dirNameoutput + str(pNumber2[0]) +"/" + str(pNumber2) + ".tiff")
            
            # 4.
            p1cols = dd_sepImageinBlocks(p1, 0)
            k = 0;
            for index in range(len(p1cols)):
                if(k == 1):
                    pargs = dd_sepImageinBlocks(p1cols[index], 1)
                    for parIndex in range(len(pargs)):
                        Image.fromarray(pargs[parIndex].astype(np.uint8)).save(dirNameoutput + str(pNumber1[0]) +"/page"+ str(pNumber1) +"block_"+ str(index+1) +"par-"+ str(parIndex)+".tiff")
                else: Image.fromarray(p1cols[index].astype(np.uint8)).save(dirNameoutput + str(pNumber1[0]) +"/page"+ str(pNumber1) +"block_"+ str(index+1) +".tiff")
                k = k + 1
              
            k = 0;  
            p2cols = dd_sepImageinBlocks(p2, 0)
            for index in range(len(p2cols)):
                if(k == 1):
                    pargs = dd_sepImageinBlocks(p2cols[index], 1)
                    for parIndex in range(len(pargs)):
                        Image.fromarray(pargs[parIndex].astype(np.uint8)).save(dirNameoutput + str(pNumber2[0]) +"/page"+ str(pNumber2) +"block_"+ str(index+1) +"par-"+ str(parIndex)+".tiff")
                else: Image.fromarray(p2cols[index].astype(np.uint8)).save(dirNameoutput + str(pNumber2[0]) +"/page"+ str(pNumber2) +"block_"+ str(index+1) +".tiff")
                k = k + 1
               
    # 5.
    # p2col1, p2col2 = dd_sepImageIn2Col(p2)
    # Image.fromarray(p2col1.astype(np.uint8)).save("D:/distribution_digitizer/2019/mytest/output/"+ str(pNumber2) +"col1.tiff")
    # Image.fromarray(p2col2.astype(np.uint8)).save("D:/distribution_digitizer/2019/mytest/output/"+ str(pNumber2) +"col2.tiff")
    
    # 6. Nur den Text col2 bearbeiten
    # This is an arbitrary threshold which seems to work. The reason why it
    # works is that we "uniformized" input images by conveting them to black and white.
    # clip_th = 254.6
    # clipped = clip_map(clip_map(p1col2, axis=0, th=clip_th), axis=1,th=clip_th)
    # Image.fromarray(clipped.astype(np.uint8)).save("D:/distribution_digitizer/2019/mytest/input/p2col1_clipped.tiff")

