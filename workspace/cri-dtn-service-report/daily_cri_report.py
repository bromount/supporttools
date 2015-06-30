'''
Created on Jun 21, 2015

@author: aarunachalam
'''
import sys
import re
import string
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
from docutils.nodes import line

ifile  = open('team_test.csv', "rb")
reader = csv.reader(ifile)

ifile1  = open('team.csv', "rb")
reader1 = csv.reader(ifile)

ctfWsdl = 'https://forge.collab.net/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('annamalai','Openthis22@!')
print "Logged in to Forge"

userid= ctf.getUserSessionBySoapId(login)

projects = ctf.getProjectList(login,False)

#This is to parse the SOAPPy output
#for item in projects:
#    for value in item:
#        print value[2],"=",value[4]

#This will print the project id and project name

data =     []

def sendmail(table,total_artifacts,receiver_email,username):
    subjectline = "[IGNORE]" +username + ", you have " +  str(total_artifacts) + "  issues in CRI Tracker"
                
    table =  "<h2>" + subjectline + "</h2>" + table
              
    copied = ['aamalai@gmail.com']
    
    sender = "annamalai@collab.net"
        
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subjectline
    msg['From'] = sender
    msg['To'] = receiver_email
    msg['Cc'] = ",".join(copied)
    emails=receiver_email.split()+copied
    html = table
        
    content = MIMEText(html, 'html')
        
    msg.attach(content)
    try:
        smtpObj = smtplib.SMTP('mail-qa1.sp.collab.net')
        if total_artifacts > 0:
            smtpObj.sendmail(sender, emails, msg.as_string())         
            print "Successfully sent email"
    except:
        print "Error: unable to send email"

def get_user_artifact(user):
    trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'
    tracker = SOAPpy.SOAPProxy(trackerWsdl)
    filter = SOAPpy.Types.structType()
    filter._addItem('SoapFilter', { 'name' : 'submittedBy', 'value' : user})
    filter._addItem('SoapFilters',{'name':'status' ,'value': 'Open'})
    filter._addItem('SoapFilter1',{'name':'status' ,'value': 'In Progress'})
    filter._addItem('SoapFilters2',{'name':'status' ,'value': 'Re-opened'})
    #filter._addItem('SoapFilters3',{'name':'status' ,'value': 'Invalid'})
    filter._addItem('SoapFilters4',{'name':'status' ,'value': 'Fixed - Verify & Close'})
        
    #proj1362 is the customer issues project
    #tracker2160 is the CRI tracker
    #tracker2168 is the DTN tracker
    tracker_id = "tracker2160" 
    artifacts = tracker.getArtifactList(login,tracker_id,filter)
    print artifacts
    return artifacts
    
                   
for row in reader:
    if row[0]:
        username = row[0]
        email = row[1]
        artifacts=get_user_artifact(username)
        counter = 0
            
        table = """
        <table border="1">
        <tr>
        <th>S.No </th>
        <th> Submitted By</th>
        <th> Artifact </th>
        <th> Title </th>
        <th> Submitted Date</th>
        </tr>
        """
        for item in artifacts:
            for value in item:
                print value['submittedDate']
                #sys.exit()
                #print type(item)
                counter = counter + 1
                submitted_time_list = list(value['submittedDate'])
                submitted_time_list=map(int, submitted_time_list)
                print submitted_time_list
                submitted_time_list.append(0)
                submitted_time_list.append(0)    
                submitted_time_list.append(0)
                submitted_time_tuple=tuple(submitted_time_list)
                print submitted_time_tuple
                #modified_time_tuple=map(int, modified_time_tuple)
                
                submitted_time = time.strftime("%m/%d/%y ", submitted_time_tuple)
                
                #To find the different between two dates
                time_tuple = value['submittedDate']
                dt_obj=datetime(*time_tuple[0:3])
                
                date_difference =  dt_obj.toordinal() - datetime.today().toordinal()
                
                if date_difference == 0:
                    #table = table + "<tr><td><b><font color='black'>" + str(counter) + "<td><b><font color='black'>" + username + "</font></b></td><td><b><font color='red'><a href=https://forge.collab.net/sf/go/" + value['id'] + ">" + value['id'] +"</a></b></font> </td> <td> <b><font color='black'> " + value['title'].encode("utf-8") + "</font></b></td><td> <b><font color='black'>" + submitted_time + "</font></b></td></tr>"
                    pass
                else:
                    table = table + "<tr><td><b><font color='black'>" + str(counter) + "</font></b></td><td><b><font color='red'><a href=https://forge.collab.net/sf/go/" + value['id'] + ">" + value['id'] +"</a></b></font> </td> <td> <b><font color='red'> " + value['title'].encode("utf-8") + "</font></b></td><td> <b><font color='black'>"  + submitted_time + "</font></b></td></tr>"

        table = table + "</table> <br> Note: Artifacts which is not updated more than 'three' days will be in <font color='red'><b>RED</b></font>."
        print table
        sendmail(table, counter,email,username)      
                
        #print data
        print "..."
        