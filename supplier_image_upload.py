#!/usr/bin/env python3

import os
import requests
import sys

# Initiate variables for source and upload path.

source_files = os.listdir('/supplier-data/images')
upload_path = 'http://localhost/upload/'

# Begin the loop to open and iterate through all the new jpeg images in the source folder.
# The loop will then make sure just to open the jpeg files.
# It will then upload them to the correct upload path

for file in source_files:
  if file.endswith('.jpeg'):
    temp = open(source + file)
    response = requests.post(upload_path, files=temp)
    #print(response.status_code)
    temp.close()
