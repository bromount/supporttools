import lxml.html.clean as clean
import urllib2
import base64
import os,fnmatch
import glob
import json
from configobj import ConfigObj
import logging
import ConfigParser
import sys
import time

config = ConfigParser.ConfigParser()
config.read('config.txt')


zendesk_url = config.get('settings','zendesk_url')
zendesk_username = config.get('settings','zendesk_username')
zendesk_password = config.get('settings','zendesk_password')


category_ctf =  config.get('settings','category_ctf')
category_faq = config.get('settings','category_faq')


forum_create_results = open("forums.txt", "a")

path = "."

logging.basicConfig(filename="forum_create.log", level=logging.INFO)


forums_ctf_file = config.get('settings','forums_ctf_file')
forums_faq_file = config.get('settings','forums_faq_file')


def create_forum(category,section_file):

    print category
    
    section_list = open(section_file,'r')



    for section in section_list:
        print section
        
        url = zendesk_url + '/api/v2/help_center/en-us/categories/' + category + '/sections.json'
        print url
        
        data = {"section": {"name":section.strip() } }
        
        jsondata = json.dumps(data)

        req = urllib2.Request(url= url, data = jsondata, headers={'Content-Type': 'application/json'})
        base64string = base64.encodestring('%s:%s' % (zendesk_username,zendesk_password)).replace('\n','')
        req.add_header("Authorization","Basic %s" % base64string)
        result = urllib2.urlopen(req)

        result_json = result.read()
    #    print r

        data = json.loads(result_json)
        
#        print data
        
        section_id = data['section']['id']
        #print url_id
        print "creating section " + section.strip()
        logging.info("created section " + section.strip())
        
        forum_create_results.write( "\n" + section.strip() + ' = ' + str(section_id) )
        
        time.sleep(1)        
        
        

create_forum(category_ctf,forums_ctf_file)
create_forum(category_faq,forums_faq_file)
