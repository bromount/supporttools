#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email.mime.base import MIMEBase
import os
import sys

'''file_open=open('20150626_cri_details_cert.html','r')

print file_open

sys.exit()'''

with open("20150626_cri_details_support.html","r") as file_open:
	lines=file_open.read()
	print lines



subjectline = "This is a test"

receiever = "annamalai@collab.net"
 
sender = "annamalai@collab.net"

msg = MIMEMultipart('alternative')

msg['Subject'] = subjectline

msg['From'] = sender

msg['To'] = receiever

html = lines

content = MIMEText(html, 'html')

msg.attach(content)
try:
	smtpObj = smtplib.SMTP('mail-qa1.sp.collab.net')
	smtpObj.sendmail(sender,receiever,msg.as_string())
	print "msg sent successfully"
except:
	print "Error in sending mail"




	
