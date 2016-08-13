#!/usr/bin/python

import subprocess
import logging
import ConfigParser
import socket
import re
from simple_salesforce import Salesforce
import platform
import time
import datetime
import sys

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')


config = ConfigParser.ConfigParser()
config.read('config.txt')

log_file = 'logs/sync-' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


report_file = 'logs/sync-details-' + timestamp + '.txt'
report = open(report_file,'wb')



#find no of active users in last 30 days

#command = "echo " +  " \"select count(distinct(created_by_id)) from audit_entry where date_created <= now() and date_created >= now() - INTERVAL '30 DAYS';\" " + " |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


#logging.info("running " + command + "command")
#p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
#no_of_active_users_in_30_days, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_active_users_in_30_days
#report.write("*** ***\n")
#report.write("No of Active users in last 30 days  = " + str(int(no_of_active_users_in_30_days)) + "\n\n")

#report.close()





salesforce_username = config.get('settings','salesforce_username')
salesforce_password = config.get('settings','salesforce_password')
salesforce_security_token = config.get('settings','salesforce_security_token')

print "hello"

sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)

try:
	print "Connecting to SalesForce..."	
	sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)


except:
	print "error"
	logging.info("Error connecting to salesforce. Check Username, password and security token in ctf-reports-config.txt")
	sys.exit(1)


query = "SELECT Name,Email,Account.Name From Contact  WHERE (Account.Support_Product__c LIKE 'ScrumWorks%' OR Account.Secondary_product__c LIKE 'ScrumWorks%') AND (Account.Type LIKE 'Customer%') AND Contact.Primary_Support_Contact__c = true  "

#query = "select a.name from contact c, account a where (a.Support_Product__c LIKE 'ScrumWorks%' Or a.Secondary_product__c LIKE 'ScrumWorks%') AND (a.Type LIKE 'Customer%') AND a.Name=c.Account AND c.Primary_Support_Contact__c='True' "

#query = "select account.name, (select contact.firstname from account.contacts) from account limit 5"
print query
people = sf.query(query)
#print people

result = open("results.csv","w")
for person in people["records"]:
    record = person["Name"] + " , " + person["Email"] +" , " + person["Account"]["Name"] + "\n"
    decoded = record.encode('ascii', 'ignore')
    result.write(decoded)

result.close()

