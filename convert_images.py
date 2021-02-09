#!/usr/bin/env python3

import os
import sys
from PIL import Image

#Define the source variable for the correct folder.
source = os.path.expanduser('~') + '/supplier-data/images/'

#Batch convert all tiff files to jpeg, resize them, and save them to the correct path.
for image in os.listdir(source):
  if 'tiff' in image:
    temp = Image.open(source + image)
    destination = '/supplier-data/images' + image.split('.')[0]
    temp.convert('RGB').resize((600, 400)).save(destination + '.jpeg')
    temp.close()
