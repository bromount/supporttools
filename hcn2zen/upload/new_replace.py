import lxml.html.clean as clean
from BeautifulSoup import BeautifulSoup
import json
import urllib2
import base64
import os
import fnmatch
import json
import glob
from configobj import ConfigObj
import logging
import time
import traceback
import sys
import shutil

username = 'annamalai@collab.net'
password = 'Collabnet1!'


try:
    config = ConfigObj('results.txt')
except Exception, err:
    print traceback.format_exc()


sitename = "https://cspl2.zendesk.com"

#title_parser = ConfigObj('titles.txt')
logging.basicConfig(filename="replace.log", level=logging.INFO)


def get_page_id(filename):
    try:
        return config.get(filename)
    except:
        print " page id error"


'''def replace_url(filename, zendeskid):
    try:
        title = title_parser.get(filename).replace(" ","-").replace("?","-")
        newurl = sitename + "/entries/" + zendeskid + "-" + title
        return newurl
    except:
        print "url error"'''

os.chdir(".")
path = "."


'''def locate(pattern, root=os.curdir):
    Locate all files matching supplied filename pattern in and below
    supplied root directory.
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)'''

all_files =  glob.glob("*html")

for htmlfile in all_files:

    #only_filename = htmlfile.split(os.sep)[-1]
    print "working on " + htmlfile
    logging.info("working on " + htmlfile)
    current_page_id = get_page_id(htmlfile)
    print current_page_id
    logging.info("its page id " + str(current_page_id))

    orig_content = open(htmlfile, 'rw').read()
    soup = BeautifulSoup(orig_content)
    result = str(soup)
    
    for img in soup.findAll('img'):
      current_image = img['src']
      if 'shared' in img['src']:
	new_image = img['src'].replace("../shared/..","http://help.collab.net/topic/teamforge720/")
        print new_image
      else:
        new_image = img['src'].replace("..","http://help.collab.net/topic/teamforge720/")
	print new_image
      img['src'] = img['src'].replace(current_image,new_image)

      logging.info("replacing image link " + current_image + "with " + new_image)
    result = str(soup) 
   
    
    for a in soup.findAll('a'):
#a['href'] = a['href'].replace("google", "mysite")
#print a['href']
        #print a
	#pageidvariable="no"
        if not a.get("href") == None:
	    print  "HREF = " + a.get("href")
	    if a.get('href').endswith('.html') :
		if not "../shared" in a.get('href'):
		  if not a.get('href').startswith('http'):
	            filename = a.get("href")
        	    print filename
	            pageid = get_page_id(filename)
	            print pageid
		    #pageidvariable="yes"
        	    new_url= sitename + '/hc/en-us/articles/' + str(pageid)
		    print new_url
	            current_href = a.get("href")

	            try:
        	        a['href'] = a['href'].replace(current_href, new_url)
	                print a['href']
	                logging.info("replacing link " + current_href + "with " + new_url)
	            except:
	                print "next"
        	    result = str(soup)

            #print result
	else:
	    result = str(soup)
    try:    
        new_content = open(htmlfile, 'w')
        new_content.write(result)
    except Exception, err:
        print traceback.format_exc()

    # To remove the meta tags
    strip = clean.Cleaner(meta = True, style = True, page_structure = True, remove_tags = ['FONT', 'font', 'span'])
    content = strip.clean_html(result)

    # To remove the title tags and contents
    cleaned_content =   content.split('\n',1)[1].split('\n',1)[1].split('\n',1)[1].split('\n',1)[1].split('</h1>',1)[1]
    cleaned_content =   cleaned_content.split('<div class="related-links">',1)[0]

#    print cleaned_content
    data = {"article": {"body": cleaned_content}}
    jsondata = json.dumps(data)

    #print"===============" +  pageidvariable 
  #  if not current_page_id == None :
    print "Replacing the file" + htmlfile
    current_page_edit_url = sitename + '/api/v2/help_center/articles/' + str(current_page_id) + '.json'
    print current_page_edit_url
    logging.info("reuploading " + current_page_edit_url)

    req = urllib2.Request(url=current_page_edit_url, data = jsondata, headers={'Content-Type': 'application/json'})
    base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
    req.add_header("Authorization","Basic %s" % base64string)
    req.get_method = lambda: 'PUT'

    result = urllib2.urlopen(req)
    print "url = " + sitename + '/hc/en-us/articles/' + str(current_page_id)
    print "moved to reuploaded folder"
    shutil.move(htmlfile,"../reuploaded")
    
time.sleep(2)
