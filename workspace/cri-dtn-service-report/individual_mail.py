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

ctfWsdl = 'http://forge.collab.net:8080/ce-soap50/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('helpdesk','Collabnet@1')
#print login

projects = ctf.getProjectList(login)
#print projects

#This is to parse the SOAPPy output
#for item in projects:
#    for value in item:
#        print value[2],"=",value[4]

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


userWsdl = 'http://forge.collab.net:8080/ce-soap50/services/CollabNet?wsdl'
userdata = SOAPpy.SOAPProxy(userWsdl)



def get_cri_count(user,status):
    tracker = SOAPpy.SOAPProxy(trackerWsdl)
    filter = SOAPpy.Types.structType()
    filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : user})
    filter._addItem('SoapFilters',{'name':'status' ,'value': status})
    
    #proj1362 is the customer issues project
    #tracker2160 is the CRI tracker
    tracker_id = "tracker2160"
    artifacts = tracker.getArtifactList(login,tracker_id, filter)
    #print artifacts
    #trackerlist = tracker.getTrackerList(login,'proj1362')
    
    
    counter = 0
    for item in artifacts:
        for value in item:
            counter = counter + 1
    return counter

support_team = {    'annamalai' : 'annamalai@collab.net',
                    'helpdesk': 'null@collab.net',
                    'support1':'null@collab.net',
                    'karishma' : 'karishma@collab.net',        
                    'jeeva' : 'jeeva@collab.net',
                    'aneeja' : 'aneeja@collab.net',
                    'annamalai' : 'annamalai@collab.net',
                    'arunp_cn' : 'arunp@collab.net',
                    'ashok_cn':'ashok@collab.net',
                    'dthomas':'dthomas@collab.net',
                    'elangos':'elangos@collab.net',
                    'jeyanthan':'jeyanthan@collab.net',
                    'karthiks':'karthiks@collab.net',
                    'manikandan':'manikandan@collab.net',
                    'mfieldhouse':'mfieldhouse@collab.net',
                    'mgokoffski':'mgokoffski@collab.net',
                    'pritha':'pritha@collab.net',
                    'ramya':'ramya@collab.net',
                    'rparedes':'rparedes@collab.net',
                    'swomiya_cn':'sowmiya@collab.net'
                    
         }      
            
 
              
# The username for Support L2 in forge is supportl1. To change the name in the mail, this function is used.

##def set_name(name):
##    if name=='support1':
##        name = "Support"+" L2"
##        return name
##    else:    
##        return name
    
    
def set_name(username):
       
    if username=='support1':
        username = "Support"+" L2"
        return username
    else:    
        forge_name = userdata.getUserData(login,username)
        first_name = forge_name.fullName.split()[0]
        return first_name





table = """
<table border="1" cellspacing="0">
<tr>
<th>S.No </th>
<th> Support Rep </th>
<th> Open</th>
<th> Considered in future release</th>
<th>In Next Release</th>

</tr>
"""



counter = 1

#here the support team list is sorted on alphabetical order
supportlist = support_team.keys()
supportlist.sort()


for person in supportlist:    
    table = table + "<tr><td align = 'center'>" + str(counter) + "</td><td>" +  set_name(person) + " </td> <td align = 'center'> "  + str(get_cri_count(person, 'Open')) + " </td> <td align = 'center'> "  + str(get_cri_count(person, 'Considered in future release')) + "</td><td align='center'>" + str(get_cri_count(person, 'In Next Release')) + "</td></tr> "
    counter = counter + 1
table = table + "</table>"

#print table



subjectline = "Open CRIs This week"

table =  "<h2>" + subjectline + "</h2>" + table


for receiver in support_team.values():
    sender = "annamalai@collab.net"
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
 #       print "Successfully sent email"
    except SMTPException:
        print "Error: unable to send email"



