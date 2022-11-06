# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:25:35 2022

@author: Kailun Sha
"""

import exifread
import os

loadfile_root = input('Please enter the photo folder path:')
loadsavepath = input('Please enter the path of the output file:')
filetype = input('Please enter the file type and the file is case sensitive:')
file_root = loadfile_root.replace('/', '//')  # route conversion
file_list = os.listdir(file_root)  # Get the names of all files in the folder


# Iterate over all files in this folder
for img_name in file_list:
    savepath = loadsavepath.replace('/', '//')  # route conversion
    txtrealpath = savepath+'/'+img_name.replace('.'+filetype,'')+'.txt'  # Get the file path of .txt
    txt = open(txtrealpath, 'w')  # create a New txt file
    realpath = file_root+'/'+img_name  # Get the file path of the image
    f = open(realpath, 'rb')  # Open file '', enter the file path
    tags = exifread.process_file(f)  # Read tags, which is a file of type dict


# Traverse the elements of the dictionary, split the key and value of each element into a string, pay attention to adding separators and newlines
    for k, v in tags.items():
        txt.write(str(k) + ':' + str(v) + '\n')
    txt.close()  # close txt
