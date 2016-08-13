import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import irclib
import csv

ifile  = open("server-details.csv","rb")
reader = csv.reader(ifile)

for row in reader:
	sitename = row[0]
	username = row[1]
	password = row[2]



delete_username = 'summa'

ctfWsdl = sitename + '/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login(username,password)
#print login

sessionid= ctf.getUserSessionBySoapId(login)

userdata = ctf.getUserData(sessionid,delete_username)

print userdata

FullName = userdata['fullName']
print FullName




new_name = FullName +'(deleted)'
#setUserData

user= SOAPpy.SOAPProxy(ctfWsdl)


#print user.__doc__
#print user.methods.keys()


#print(user.soapproxy.namespace)
#print(user.soapproxy.soapaction)
#print(user.wsdl)

filter = SOAPpy.Types.structType()
filter._addItem('status', SOAPpy.stringType('Removed'))
filter._addItem('fullName',SOAPpy.stringType(new_name))
filter._addItem('username',SOAPpy.StringType(delete_username))


#user_details = {'username':delete_username, 'status':'Removed','licenseType':'ALM'}


user_details = {'status': 'Removed',  'licenseType': 'ALM',   'username': 'summa', 'version': 110,  'id': 'user1048',  'fullName': 'summa(expired)', 'email': 'summa@summa.com'}

import pdb; pdb.set_trace()
usersoapdo = SOAPpy.Types.structType(data=user_details, name='delete_user')
usersoapdo1 = SOAPpy.Types.structType(user_details)

u1 = user.setUserData(sessionid,usersoapdo1)
u = user.setUserData(sessionid,usersoapdo)
print u


#projects = ctf.getProjectList(login,False)
#print projects

#print type(projects)
#print len(projects)

#This is to parse the SOAPPy output
#for item in projects:
#	for value in item:
#		print value[2],"=",value[4]

#This will print the project id and project name

#trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'
#tracker = SOAPpy.SOAPProxy(trackerWsdl)
#filter = SOAPpy.Types.structType()
#filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : 'helpdesk'})
#filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
#filter._addItem('SoapFilter', {  'assignedToUsername': 'support1', 'statusClass':'Open'})

#filter._addItem('assignedToUsername', 'support1')
#filter._addItem('status','Open')
#filter = {  'assignedToUsername': 'support1', 'statusClass':'Open'}

#print filter

#def get_artifacts(tracker_id):
 
#proj1362 is the customer issues project
#tracker2160 is the CRI tracker
#tracker2168 is the DTN tracker
#tracker_id = "tracker2168" 
#artifacts = tracker.getArtifactList(login,tracker_id, filter)
#print artifacts
#trackerlist = tracker.getTrackerList(login,'proj1362')
#print trackerlist

               
#artifact objct has 24 elements
#12 is artifact no and 24 is title

#for item in artifacts:
#	for value in item:
#		print value[1]
#		print value[2]
#		print value[3]
#		print value[4]
#		print value[5]
#		print value[6]	
#		print value[7]
#		print value[8]
#		print value[9]
#		print value[10]
#		print value[11]
#		print value[12]
#		print value[13]
#		print value[14]		
#		print value[15]
#		print value[16]
#		print value[17]
#		print value[18]
#		print value[19]
#		print value[20]
#		print value[21]
#		print value[22]
#		print value[23]
#		print value[24]
#		print value[25]
#		print value[26]
#		print value[27]

		


