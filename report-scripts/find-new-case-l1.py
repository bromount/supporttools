#!/usr/bin/python
#script to find new case in l1 queue and to ping in #level1 channel

import feedparser
import irclib
import re
import time


# Connection information
network = 'irc.collab.net'
port = 6667
channel = '#level1'
#nick = 'NewCase'
name = 'shrinivasan'

# Connect
irc = irclib.IRC()
server = irc.server()
#server.connect ( network, port, nick, ircname = name )


#The New case alerts are sent to the discussion "CSR_Queue" discussion in the https://crm.extranet.collab.net
#https://crm.extranet.collab.net/servlets/WebFeed?artifact=messages&dsForumId=2928 is the RSS feed for the discussion
#adding username and password to get the feeds
try:
	d=feedparser.parse('https://pcnbot:PCN@robot1@crm.extranet.collab.net/servlets/WebFeed?artifact=messages&dsForumId=2928')
except:
	exit(0)

#The file archive.txt has the id for last RSS feed

with open('/home/support/python/archieves.txt', 'rb') as record:
	first_line = record.readline()


count = 0
for entry in d.entries:
	
	if first_line.strip() == entry.id.strip():
		break
	else:
		count = count + 1
#		print entry.id
#		print entry.title
#		print entry.description	
		
		try:				
			title = entry.title.split(" - ")
			caseno = title[0]
			priority = title[2].split()[0]
			subject = entry.description.split("Case Subject :")[1].split("\n")[0]
#			print subject
			message = caseno + " - " + priority + subject
#			print message
		except IndexError:
			message = caseno
		
		try:		
			url = re.findall('(https://[^"\' ]+)',entry.description)		
			ping_message = message +"  - "+  url[0]
		except:
			ping_message = message

		if "New Case" in entry.title:
			nick = "NewCase"
		elif "New case comment" in entry.title:
			nick = "NewComment"
		elif "New case attachment" in entry.title:
			nick = "NewAttachment"
		
		if not "collab.net" in entry.author_detail.email:			
			server.connect ( network, port, nick, ircname = name )
			server.privmsg("#level1", ping_message)
			time.sleep(5)



with open('/home/support/python/archieves.txt', 'w') as record:
	record.write(d.entries[0].id)
	record.close()	



