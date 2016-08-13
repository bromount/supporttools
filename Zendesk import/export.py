import json
import urllib2
import base64
import os
import glob

os.chdir(".")
for files in glob.glob("*.html"):
	print files
	username = 'MyMail@company.com'
	password = 'MyPassword'
	ext_file=files
	content = open(ext_file, 'r').read()
	title = open(ext_file, 'r').read().split('<title>')[1].split('</title>')[0].strip()
	print title
	data = {"topic": {"forum_id": 21802721, "title": title, "body": content, "topic_type": "articles", "access": "logged in users" } }
	jsondata = json.dumps(data)

	req = urllib2.Request(url='https://ctfdocs.zendesk.com/api/v2/topics.json', data = jsondata, headers={'Content-Type': 'application/json'})
	base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
	req.add_header("Authorization","Basic %s" % base64string)
	result = urllib2.urlopen(req)
