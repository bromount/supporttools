import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from operator import itemgetter

ifile  = open('team.csv', "rb")
reader = csv.reader(ifile)


ifile1  = open('team.csv', "rb")
reader1 = csv.reader(ifile)


ctfWsdl = 'https://forge.collab.net/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('shrinivasan','Vanakkam@3')
print login

userid= ctf.getUserSessionBySoapId(login)

projects = ctf.getProjectList(login,False)
#print projects

#print type(projects)
#print len(projects)

#This is to parse the SOAPPy output
#for item in projects:
#	for value in item:
#		print value[2],"=",value[4]

#This will print the project id and project name

data = 	[]

def count_artifact(user):
	trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'
	tracker = SOAPpy.SOAPProxy(trackerWsdl)
	filter = SOAPpy.Types.structType()
	filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : user})
	filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
	filter._addItem('SoapFilter1',{'name':'status' ,'value': 'In Progress'})
	filter._addItem('SoapFilters2',{'name':'status' ,'value': 'Re-opened'})


	#proj1362 is the customer issues project
	#tracker2160 is the CRI tracker
	#tracker2168 is the DTN tracker

	cri = "tracker2160" 
	cri_artifacts = tracker.getArtifactList(login,cri, filter)
	cri_count = len(cri_artifacts[0])

	dtn = "tracker2168"
	dtn_artifacts = tracker.getArtifactList(login,dtn, filter)
        dtn_count = len(dtn_artifacts[0])

	userdata = ctf.getUserData(login,user)
	fullname =  userdata['fullName']
#	global data
	data.append([fullname,cri_count,dtn_count])


counter = 0

table = """
<table  border="1">
<tr>
<th >S.No </th>
<th > Support Rep</th>
<th width="10px"> CRI </th>
<th width="10px"> DTN</th>
</tr>
"""




for row in reader:
	
	if row[0]:
		username = row[0]
	count_artifact(username)

	print data

ifile.seek(0,0)


# to sort the list 
sorted_data = sorted(data, key=itemgetter(1,2), reverse = True)


#print "\n sorted data \n"

print sorted_data



for item in sorted_data:
	print item
	table = table + "<tr><td>" + str(counter + 1) + "</td><td>" + str(sorted_data[counter][0]) + "</td><td>" + str(sorted_data[counter][1]) + "</td><td>" + str(sorted_data[counter][2]) + "</td></tr> "
	counter = counter + 1
	
	print table

print table

subjectline = "Open CRI/DTN Report - Via Script"

table =  "<h2>" + subjectline + "</h2>" + table

Team = ['shrinivasan@collab.net']


for receiver in Team:
	sender = "shrinivasan@collab.net"
#receiver  = "shrinivasan@collab.net"


	msg = MIMEMultipart('alternative')
	msg['Subject'] = subjectline
	msg['From'] = sender
	msg['To'] = receiver

	html = table
	
	content = MIMEText(html, 'html')

	msg.attach(content)
	try:
	   smtpObj = smtplib.SMTP('maa-exchmb.maa.corp.collab.net')
	   smtpObj.sendmail(sender, receiver, msg.as_string())         
	   print "Successfully sent email"
	except:
	   print "Error: unable to send email"


#get_artifacts('tracker2160')
#sendmail()

