#!/usr/bin/env python3

import os
import requests
import sys

# Initiate variables to set path and external IP

source_path = 'supplier-data/descriptions'
source_full = os.listdir(source_path)
upload_path = 'http://localhost/fruits/'

# Begin the loop to open and iterate through all files in the source folder.
# The loop will then make sure not to open any strange temp files.
# It will open them, read them, and split the new lines for our dictionary.
# Finally, it will post the review and grab a http status code.

for file in source_full:
  if file.endswith('.txt'):
    image_name = os.path.splitext(file)[0]
    temp = open(source_path + file)
    data = temp.read().split('\n')
    fruit_dict = {"name":data[0], "weight":int(data[1].strip(" lbs")), "description":data[2], "image_name": image_name + ".jpeg"}
    response = requests.post(upload_path, json=fruit_dict)
    print(response.status_code)
