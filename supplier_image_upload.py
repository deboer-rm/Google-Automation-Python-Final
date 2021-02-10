#!/usr/bin/env python3

import os
import requests
import sys

# Initiate variables for source and upload path.

source_path = 'supplier-data/images/'
source_full = os.listdir(source_path)
upload_path = 'http://localhost/upload/'

# Begin the loop to open and iterate through all the new jpeg images in the source folder.
# The loop will then make sure just to open the jpeg files.
# It will then upload them to the correct upload path

for file in source_full:
  if file.endswith('.jpeg'):
    with open(source_path + file, 'rb') as opened:
      response = requests.post(upload_path, files={'file': opened})
      #print(response.status_code)
