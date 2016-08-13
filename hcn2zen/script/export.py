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
import shutil

config = ConfigParser.ConfigParser()
config.read('config.txt')


zendesk_url = config.get('settings','zendesk_url')
zendesk_username = config.get('settings','zendesk_username')
zendesk_password = config.get('settings','zendesk_password')


category_ctf =  config.get('settings','category_ctf')

forums_file = ConfigObj('forums.txt')


upload_results = open("results.txt", "a")

path = "."

logging.basicConfig(filename="export.log", level=logging.INFO)


def get_section_id(section_name):
    return forums_file.get(section_name)


def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

all_files = locate("../newhtml/*.html")

for filename in all_files:
    print filename
    
    only_filename = filename.split(os.sep)[-1]
    logging.info("fixing the file" + filename)

    orig_content = open(filename, 'r').read()
    title = open(filename, 'r').read().split('<title>')[1].split('</title>')[0].strip()
    print title

    with open(filename, 'r') as file_open:
       	content=file_open.readlines()

        #print content
        for line in content:
                if "name=\"DC.Coverage\"" in line:
                        coverage=line.split("content")[1].strip("=").strip('"').strip('>').split("\"")[0]
                        #print line.strip('"/>')
                        print coverage

                if "name=\"keywords\"" in line:
                        keywd=line.split("content")[1].strip("=").strip('"').split("\"")[0].split(",")
                        print keywd

                if "name=\"prodname\"" in line:
                        prodname=line.split("content")[1].strip("=").strip('"').split("\"")[0]
                        print prodname

                if "name=\"version\"" in line:
                        version=line.split("content")[1].strip("=").strip('"').split("\"")[0]
                        print version


    section_id=get_section_id(coverage)

# To remove the meta tags
    strip = clean.Cleaner(meta = True, style = True, page_structure = True, remove_tags = ['FONT', 'font', 'span', 'h1'])
    content = strip.clean_html(orig_content)

# To remove the title tags and contents
    cleaned_content = content.split('\n',1)[1].split('\n',1)[1].split('\n',1)[1].split('\n',1)[1]
    cleaned_content = cleaned_content+"\n \n "+"Valid For : " +prodname+" "+version
#    print filecontent
    print filename
    print section_id
    try:

        logging.info("uploading " + filename + " to " + section_id)
    
        data = {"article": {"locale":"en-us","title": title, "body": cleaned_content, "label_names":keywd} }
        jsondata = json.dumps(data)
        
        req = urllib2.Request(url=zendesk_url+'/api/v2/help_center/sections/'+str(section_id)+'/articles.json', data = jsondata, headers={'Content-Type': 'application/json'})
        base64string = base64.encodestring('%s:%s' % (zendesk_username,zendesk_password)).replace('\n','')
        req.add_header("Authorization","Basic %s" % base64string)
    
#    try:
    
    	result = urllib2.urlopen(req)
        result_json = result.read()
#    print r

    	data = json.loads(result_json)

        url_id = data['article']['id']
        print url_id

        upload = only_filename + " = " + str(url_id) + "\n"
        print upload

        logging.info("uploaded topic id " + upload)
        upload_results.write(upload)

        shutil.move(filename,"../upload/")
    except TypeError:
        output = open("output.txt","a")
        errstring = coverage + " & " + filename +"\n"
        output.write(errstring)
        print "Error in : " + coverage
        shutil.move(filename,"../error/")
upload_results.close()
