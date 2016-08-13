#!/usr/bin/python
# -*- coding: utf-8 -*-

#script to backup the zendesk articles

#provide all required information at config.txt

#author Shrinivasan <shrinivasan@collab.net>



from ConfigParser import SafeConfigParser
import logging
import urllib2
import base64
import json
import datetime
import shutil
import os
import tarfile
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import traceback
import sys




now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M")

tarfilename = timestamp + '.tar.gz'

logging.basicConfig(filename="export.log", level=logging.DEBUG)

parser = SafeConfigParser()
parser.read('config.txt')

sitename = parser.get('settings', 'site')
username =  parser.get('settings', 'username')
password = parser.get('settings', 'password')
sender = parser.get('settings','email_from')
receiver = parser.get('settings','email_to')

logging.debug(timestamp)
logging.debug("backup-start")
print "Download started"


def backup_topic(topicid):
    url = sitename + '/api/v2/topics/' + str(topicid) + '.json'
    
    req = urllib2.Request(url= url,  headers={'Content-Type': 'application/json'})
    base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
    req.add_header("Authorization","Basic %s" % base64string)
    result = urllib2.urlopen(req)

    result_json = result.read()

    data = json.loads(result_json)


    body = data['topic']['body']

    title = data['topic']['title']

    title = title.replace('/','-')
    filename = "_".join( title.split() ) + ".html"

    page =codecs.open( filename,'w', encoding='utf8')
    page.write(body)
    page.close

    logging.debug("Writing into " + filename )
    print "Writing into " + filename


def backup_files():
    

    if not os.path.exists(timestamp):
        os.mkdir(timestamp)

    source = os.listdir("./")
    destination =  timestamp
    for files in source:
        if files.endswith(".html"):
            shutil.copy(files,destination)
	    os.remove(files)

    source_dir = timestamp

    with tarfile.open(tarfilename, "w:gz") as tar:
	tar.add(source_dir, arcname=os.path.basename(source_dir))


    logging.debug("Compressing files into " + tarfilename)
    print "Compressing files into " + tarfilename



all_topics = []

def get_all_topics():

    url = sitename + '/api/v2/topics.json'
#    print url
    req = urllib2.Request(url= url,  headers={'Content-Type': 'application/json'})
    base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
    req.add_header("Authorization","Basic %s" % base64string)
    result = urllib2.urlopen(req)

    result_json = result.read()

    data = json.loads(result_json)

    topics = data['topics']
    for topic in topics:
	all_topics.append( topic['id'] )
    
    return all_topics

#    print topics



article_ids =  get_all_topics()

for  article_id in article_ids:
#	print article_id
	if article_id:
		print "Downloading " + str(article_id)
		logging.debug("Downloading " + str(article_id))
 
		backup_topic(article_id)




print "\n"

print "Cleaning Files"
logging.debug("Cleaning Files")

backup_files()


print "\n\n"

print "Total files downloaded : " + str(len(article_ids))
logging.debug("Total files downloaded : " + str(len(article_ids)))

print "Backup filename =  " + tarfilename
logging.debug("Backup filename =  " + tarfilename)


print "\n\n"
print "Backup completed"
logging.debug("Backup completed")






# To send email


def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = sender
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   try:
      smtpObj = smtplib.SMTP('chennaimail.collab.net')
      smtpObj.sendmail(sender, receiver, msg.as_string())         
#      print "Successfully sent email"

      logging.debug("sent email to " + receiver)
      print "Sent email to " + receiver

   except Exception, err:
      print "Error: unable to send email"
      print traceback.format_exc()  

body = "backup for " + timestamp + "\n Remove the body and forward to artf164317@forge.collab.net "

mail(receiver,"zendesk backup "+ sitename ,body,tarfilename)

print "\n"
print "Bye."
