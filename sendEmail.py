#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
import sys
import ssl
from email.mime.text import MIMEText

sender = "crst.zh@gmail.com"
password = "bngljpsmdpbdqkvy"
def main():
   if len(sys.argv) != 4:
      sys.exit(1)
   subject, receiver, content = sys.argv[1:]
   print(subject, receiver, content)
   send_mail(subject, receiver, content)

def send_mail(sub, receiver, content):
   try:
      to = receiver
      msg = MIMEText(content, "plain")
      msg['Subject'] = sub
      msg['From'] = sender
      msg['To'] = to
      context = ssl.create_default_context()
      with smtplib.SMTP('smtp.gmail.com', 587) as server:
         server.starttls(context=context)
         server.login(sender, password)
         server.sendmail(sender, to, msg.as_string())
         print("Mail Sent Successfully")
   except Exception as e:
      print("Email Lib: Exception hit while sending email: %s"%(e))

if __name__=="__main__":
   #Send Email
   main()
