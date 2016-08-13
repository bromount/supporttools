import SOAPpy
import smtplib
import time
import datetime
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



ctfWsdl = 'https://forge.collab.net/ce-soap60/services/CollabNet?wsdl'

ctf = SOAPpy.SOAPProxy(ctfWsdl)     

login = ctf.login('helpdesk','Collabnet@1')
#print login

userid= ctf.getUserSessionBySoapId(login)


projects = ctf.getProjectList(login,False)
#print projects



#This is to parse the SOAPPy output
#for item in projects:
#	for value in item:
#		print value[2],"=",value[4]

#This will print the project id and project name

trackerWsdl = 'https://forge.collab.net/ce-soap60/services/TrackerApp?wsdl'


support_rep = 'shrinivasan'

tracker = SOAPpy.SOAPProxy(trackerWsdl)
filter = SOAPpy.Types.structType()
filter._addItem('SoapFilter', { 'name' : 'assignedTo', 'value' : support_rep})
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

def getCaseNumber(artifact):
	arti = tracker.getArtifactData(userid, artifact)
#	arti[10][2][1] is the CRM case number	
#	print arti
	return arti[10][2][1]
	



#for item in arti:
#	print  item




for item in artifacts:
	for value in item:
                print  value[13]
		print getCaseNumber(value[13])
# value[13] is the artifact id
		


