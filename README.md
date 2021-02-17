# Google-Automation-Python-Final

This repository contains scripts for the final project of Google's IT Automation with Python Professional Certificate program.

##### changeImage.py

This script will grab .tiff files in the "images" folder and convert them to .jpeg while setting a new resolution.

##### emails.py

This script is the backbone for generating emails and sending them for the health_check.py script and the report_email script.

##### health_check.py

This script will grab some stats of the computer and check things like CPU usage, a valid localhost, free disk space, pending reboots, etc.
It will send out messages using the emails.py script if any of the tests fail.
It is intended to be set to run every 60 seconds for optimal logging and performance.

##### reports.py

This script initializes the different types of reportlab objects for use in the PDF that is generated and sent via email.

##### report_email.py

This script generates a PDF from supplier .txt description files. It then sends the newly generated PDF via email.

##### run.py

This script is similar to the report_email.py script except it opens the supplier .txt description files, processes them, and post them to our website.

##### supplier_image_upload.py

This script iterates through the converted images folder (looking only for .jpeg files) and posts them to our website. 

## MORE TO FOLLOW
