import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import irclib



ctfWsdl = 'https://forge.collab.net/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('helpdesk','Collabnet@1')
#print login

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

trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'
tracker = SOAPpy.SOAPProxy(trackerWsdl)
filter = SOAPpy.Types.structType()
filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : 'helpdesk'})
filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
#filter._addItem('SoapFilter', {  'assignedToUsername': 'support1', 'statusClass':'Open'})

#filter._addItem('assignedToUsername', 'support1')
#filter._addItem('status','Open')
#filter = {  'assignedToUsername': 'support1', 'statusClass':'Open'}

#print filter

#def get_artifacts(tracker_id):
 
#proj1362 is the customer issues project
#tracker2160 is the CRI tracker
#tracker2168 is the DTN tracker
tracker_id = "tracker2168" 
artifacts = tracker.getArtifactList(login,tracker_id, filter)
#print artifacts
trackerlist = tracker.getTrackerList(login,'proj1362')
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
	count = 0
	for value in item:
		
		counter = counter + 1
		int_list = [int(i) for i in list(value[14])]
		modified_time_list = int_list
		modified_time_list.append(0)
		modified_time_list.append(0)	
		modified_time_list.append(0)
		modified_time_tuple=tuple(modified_time_list)
#		print modified_time_tuple
		modified_time = time.strftime("%m/%d/%y %H:%M:%S", modified_time_tuple)


#To find the different between two dates
		time_tuple = int_list
		dt_obj=datetime(*time_tuple[0:6])

		date_difference =  dt_obj.toordinal() - datetime.today().toordinal()
		
		table = table + "<tr><td>" + str(counter) + "</td><td><a href=https://forge.collab.net/sf/go/" + value[13] + ">" + value[13] +"</a> </td> <td> " + value[27].encode("utf-8") + "</td><td>" + modified_time + "</td></tr> "
		count = count + 1 
	

table = table + "</table>"
#print table


#def sendmail():
total_artifacts =  len(item)
subjectline = "Support Helpdesk has " +  str(total_artifacts) + "  issues in DTN Tracker"

table =  "<h2>" + subjectline + "</h2>" + table

L1Team = ['helpdesk@collab.net','shrinivasan@collab.net']


for receiver in L1Team:
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
channel = '#helpdesk'
nick = 'dtn'
name = 'shrinivasan'

# Connect
irc = irclib.IRC()
server = irc.server()
server.connect ( network, port, nick, ircname = name )

# Message both the channel and you
#server.privmsg ( channel, 'PRIVMSG to a channel.' )
#server.privmsg ( me, 'identify shrini shrini' )

if total_artifacts > 0:
        server.privmsg ( '#helpdesk', subjectline  )




#irc.process_forever()

time.sleep(5)

