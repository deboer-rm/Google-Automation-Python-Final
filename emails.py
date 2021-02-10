#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

#This function generates the email, first defaulting to no attachment
def generate_email(sender, recipient, subject, body, attachment_path = None):
  # Basic Email formatting
  message = email.message.EmailMessage()
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = recipient
  message.set_content(body)

  if attachment_path != None:
    attachment_name = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, 'rb') as fp:
      message.add_attachment(fp.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_name)
  return message

# This function sends the email to the configured SMTP server.
def send_email(package):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(package)
  mail_server.quit()
