import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import irclib



ctfWsdl = 'http://forge.collab.net:8080/ce-soap50/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('helpdesk','Collabnet@1')
#print login


projects = ctf.getProjectList(login)
#print projects

#print type(projects)
#print len(projects)

#This is to parse the SOAPPy output
#for item in projects:
#	for value in item:
#		print value[2],"=",value[4]

#This will print the project id and project name

trackerWsdl = 'http://forge.collab.net:8080/ce-soap50/services/TrackerApp?wsdl'
tracker = SOAPpy.SOAPProxy(trackerWsdl)
filter = SOAPpy.Types.structType()
filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : 'support1'})
filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
#filter._addItem('SoapFilter', {  'assignedToUsername': 'support1', 'statusClass':'Open'})

#filter._addItem('assignedToUsername', 'support1')
#filter._addItem('status','Open')
#filter = {  'assignedToUsername': 'support1', 'statusClass':'Open'}

#print filter

#def get_artifacts(tracker_id):
 
#proj1362 is the customer issues project
#tracker2160 is the CRI tracker
tracker_id = "tracker2160"
artifacts = tracker.getArtifactList(login,tracker_id, filter)
#print artifacts
trackerlist = tracker.getTrackerList(login,'proj1362')
#print trackerlist

               
#artifact objct has 24 elements
#12 is artifact no and 24 is title

#for item in artifacts:
#	for value in item:
#		print value[12],"=",value[23].encode("utf-8")
			
table = """
<table border="1">
<tr>
<th>S.No </th>
<th> Artifact </th>
<th> Title </th>
<th> Last Modified </th>
</tr>
"""

#value[13] is the modified time of the artifact.
#the type of valie[13] is a tuple.

#It has only 6 values
#to convert it to a proper datetime value, it should have 9 values.
#so converting it to a list, add three 0s, again converting to tuple.

counter = 0

for item in artifacts:
	for value in item:
#		print type(item)
		counter = counter + 1
		modified_time_list = list(value[13])
		modified_time_list.append(0)
		modified_time_list.append(0)	
		modified_time_list.append(0)
		modified_time_tuple=tuple(modified_time_list)
		print modified_tuple
#		modified_time = time.strftime("%m/%d/%y %H:%M:%S", modified_time_tuple)


#To find the different between two dates
		time_tuple = value[13]
		dt_obj=datetime(*time_tuple[0:6])

		date_difference =  dt_obj.toordinal() - datetime.today().toordinal()

		if date_difference >= -3:
			table = table + "<tr><td><b><font color='red'>" + str(counter) + "</font></b></td><td><b><font color='red'><a href=https://forge.collab.net/sf/go/" + value[12] + ">" + value[12] +"</a></b></font> </td> <td> <b><font color='red'> " + value[23].encode("utf-8") + "</font></b></td><td> <b><font color='red'>" + modified_time + "</font></b></td></tr> "
		else:
			table = table + "<tr><td>" + str(counter) + "</td><td><a href=https://forge.collab.net/sf/go/" + value[12] + ">" + value[12] +"</a> </td> <td> " + value[23].encode("utf-8") + "</td><td>" + modified_time + "</td></tr> "

table = table + "</table> <br> Note: Issues assigned in last 3 days are shown in <font color='red'><b>Red</b></font>."
#print table


#def sendmail():
total_artifacts =  len(item)
subjectline = "Support L2 has " +  str(total_artifacts) + "  issues in CRI Tracker"

table =  "<h2>" + subjectline + "</h2>" + table

L2Team = ['shrinivasan@collab.net','jeeva@collab.net','karishma@collab.net','aneeja@collab.net','manikandan@collab.net','dthomas@collab.net','mgokoffski@collab.net','annamalai@collab.net','mfieldhouse@collab.net','arunp@collab.net']


for receiver in L2Team:
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
	   if total_artifacts > 0: 
		   smtpObj.sendmail(sender, receiver, msg.as_string())         
#	   print "Successfully sent email"
	except SMTPException:
	   print "Error: unable to send email"


#get_artifacts('tracker2160')
#sendmail()



# Set this variable to your nickname
#me = 'robo'

# Connection information
network = 'irc.collab.net'
port = 6667
channel = '#troppus'
nick = 'cri'
name = 'shrinivasan'

# Connect
irc = irclib.IRC()
server = irc.server()
server.connect ( network, port, nick, ircname = name )

# Message both the channel and you
#server.privmsg ( channel, 'PRIVMSG to a channel.' )
#server.privmsg ( me, 'identify shrini shrini' )

if total_artifacts > 0:
        server.privmsg ( '#troppus', subjectline  )




#irc.process_forever()

time.sleep(5)

