#!/usr/bin/env python3

import emails
import os
import shutil
import sys
import socket
import psutil

#Returns True if the computer has a pending reboot, False otherwise.
def check_reboot():
    return os.path.exists("/run/reboot-required")

#Initialize the 3 variables and calculations for checking free disk space.
def check_disk_full(disk, min_gigabytes, min_percent):
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gigabytes or percent_free < min_percent:
        return True
    return False

#Returns True if the disk space has less than 4GB or 20% free, False otherwise.
def check_root_full():
    return check_disk_full(disk="/", min_gigabytes=4, min_percent=20)
    
#Returns True if the cpu has more than 80% usage, False otherwise.
def check_cpu_constrained():
    return psutil.cpu_percent(1) > 80
    
#Returns True if free memory is less than 500MB, False otherwise.
def check_free_memory():
    free_memory = psutil.virtual_memory().available
    # Convert to megabytes
    free_memory_MB = free_memory / 1024 ** 2
    return free_memory_MB < 500

#Returns True if the hostname "localhost" is not "127.0.0.1", False otherwise.
def check_localhost():
    local_host_ip = socket.gethostbyname('localhost')
    return local_host_ip != "127.0.0.1"

#This initializes the different email variables including the subject which will contain the type of error. 
#It relies on the email.py script.
def email_notify(error_message):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = error_message
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send_email(message)

#Validate the different computer check results and set the subject if necessary. 
if check_reboot():
  subject = "Error - System has a pending reboot"
  email_notify(subject)
  
if check_root_full():
  subject = "Error - Available disk space is less than 20%"
  email_notify(subject)

if check_cpu_constrained():
  subject = "Error - CPU usage is over 80%"
  email_notify(subject)

if check_free_memory():
  subject = "Error - Available memory is less than 500MB"
  email_notify(subject)

if check_localhost():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  email_notify(subject)
