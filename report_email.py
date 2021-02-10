#!/usr/bin/env python3

import os, datetime
import reports
import emails

# Get the current timestamp in GMT and set the source path for the dictionary files.
timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
source_path = 'supplier-data/descriptions/'

def generate_pdf(source_path):
  pdf = ""
  files = os.listdir(source_path)
  for file in files:
    if file.endswith('.txt'):
      with open(source_path + file, 'r') as f:
        inline = f.readlines()
        name = inline[0].strip()
        weight = inline[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  title = "Process Updated on " + timestamp
  # Call the reports script and generate the PDF
  package = generate_pdf(path)
  reports.generate_report("/tmp/processed.pdf", title, package)

  # Initialize email parameters
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  
  # Generate the email and send it with all parameters and attachments.
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)
