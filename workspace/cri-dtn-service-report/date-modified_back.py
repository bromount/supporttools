'''
Created on Jun 20, 2015

@author: aarunachalam
'''
import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
##import irclib



ctfWsdl = 'https://forge.collab.net/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('annamalai','Openthis22@!')
print "Logged in to Forge"
#print login


projects = ctf.getProjectList(login,False)
#print projects

#print type(projects)
#print len(projects)

#This is to parse the SOAPPy output
#for item in projects:
#    for value in item:
#        print value[2],"=",value[4]

#This will print the project id and project name

trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'
tracker = SOAPpy.SOAPProxy(trackerWsdl)
filter = SOAPpy.Types.structType()
filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : 'annamalai'})
filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
#filter._addItem('SoapFilter', {  'assignedToUsername': 'support1', 'statusClass':'Open'})
filter._addItem('SoapFilter1',{'name':'status' ,'value': 'In Progress'})
filter._addItem('SoapFilters2',{'name':'status' ,'value': 'Re-opened'})
#filter._addItem('SoapFilters3',{'name':'status' ,'value': 'Invalid'})
filter._addItem('SoapFilters4',{'name':'status' ,'value': 'Fixed - Verify & Close'})
#filter._addItem('assignedToUsername', 'support1')
#filter._addItem('status','Open')
#filter = {  'assignedToUsername': 'support1', 'statusClass':'Open'}

#print filter

#def get_artifacts(tracker_id):
 
#proj1362 is the customer issues project
#tracker2160 is the CRI tracker
#tracker2168 is the DTN tracker
tracker_id = "tracker2160" 
artifacts = tracker.getArtifactList(login,tracker_id,filter)
print artifacts
#sys.exit()
trackerlist = tracker.getTrackerList(login,'proj1362')
#print trackerlist

               
#artifact objct has 24 elements
#12 is artifact no and 24 is title

#for item in artifacts:
#    for value in item:
#        print value[12],"=",value[23].encode("utf-8")
            
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
        print value['lastModifiedDate']
        #print type(item)
        counter = counter + 1
        modified_time_list = list(value['lastModifiedDate'])
        modified_time_list=map(int, modified_time_list)
        print modified_time_list
        modified_time_list.append(0)
        modified_time_list.append(0)    
        modified_time_list.append(0)
        modified_time_tuple=tuple(modified_time_list)
        print modified_time_tuple
        #modified_time_tuple=map(int, modified_time_tuple)
        
        modified_time = time.strftime("%m/%d/%y ", modified_time_tuple)


#To find the different between two dates
        time_tuple = value['lastModifiedDate']
        dt_obj=datetime(*time_tuple[0:3])

        date_difference =  dt_obj.toordinal() - datetime.today().toordinal()

        if date_difference >= -1:
            table = table + "<tr><td><b><font color='red'>" + str(counter) + "</font></b></td><td><b><font color='red'><a href=https://forge.collab.net/sf/go/" + value['id'] + ">" + value['id'] +"</a></b></font> </td> <td> <b><font color='red'> " + value['title'].encode("utf-8") + "</font></b></td><td> <b><font color='red'>" + modified_time + "</font></b></td></tr> "
        else:
            table = table + "<tr><td>" + str(counter) + "</td><td><a href=https://forge.collab.net/sf/go/" + value['id'] + ">" + value['id'] +"</a> </td> <td> " + value['title'].encode("utf-8") + "</td><td>" + modified_time + "</td></tr> "

table = table + "</table> <br> Note: This is a <font color='red'><b>Test</b></font>."
print table


#def sendmail():
total_artifacts =  len(item)
subjectline = "You have " +  str(total_artifacts) + "  issues in CRI Tracker"

table =  "<h2>" + subjectline + "</h2>" + table

Team = ['annamalai@collab.net']


for receiver in Team:
    sender = "annamalai@collab.net"
    copied = str(['karishma@collab.net','kdani@collab.net','jeeva@collab.net'])
#receiver  = "annamalai@collab.net"


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subjectline
    msg['From'] = sender
    msg['To'] = receiver
    msg['Cc'] = ",".join(copied)

    html = table

    content = MIMEText(html, 'html')

    msg.attach(content)
    try:
       smtpObj = smtplib.SMTP('mail-qa1.sp.collab.net')
       if total_artifacts > 0:
           smtpObj.sendmail(sender, receiver, msg.as_string())         
	   print "Successfully sent email"
    except SMTPException:
       print "Error: unable to send email"


#get_artifacts('tracker2160')
#sendmail()






# Set this variable to your nickname
#me = 'robo'
'''
# Connection information
network = 'irc.collab.net'
port = 6667
channel = '#level1'
nick = 'cri'
name = 'annamalai'

# Connect
irc = irclib.IRC()
server = irc.server()
server.connect ( network, port, nick, ircname = name )

# Message both the channel and you
#server.privmsg ( channel, 'PRIVMSG to a channel.' )
#server.privmsg ( me, 'identify shrini shrini' )

if total_artifacts > 0:
    server.privmsg ( '#level1', subjectline  )




#irc.process_forever()
'''
time.sleep(5)
