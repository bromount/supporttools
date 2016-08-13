#!/usr/bin/env python
# -*- coding: utf-8 -*-



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
import json
import codecs


ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')


config = ConfigParser.ConfigParser()
config.read('config.txt')

log_file = 'logs/sync-' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


report_file = 'logs/sync-details-' + timestamp + '.txt'
report = open(report_file,'wb')

salesforce_username = config.get('settings','salesforce_username')
salesforce_password = config.get('settings','salesforce_password')
salesforce_security_token = config.get('settings','salesforce_security_token')


def search_in_salesforce():
    sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)

    try:
	    print "Connecting to SalesForce..."	
	    sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)


    except:
	    print "error"
	    logging.info("Error connecting to salesforce. Check Username, password and security token in ctf-reports-config.txt")
	    sys.exit(1)



    query = "SELECT Name,Email,Account.Name From Contact  WHERE (Account.Support_Product__c LIKE 'ScrumWorks%' OR Account.Secondary_product__c LIKE 'ScrumWorks%') AND (Account.Type LIKE 'Customer%') AND Contact.Primary_Support_Contact__c = true  "



    people = sf.query(query)



    resultfile = codecs.open("scrumworks-users-in-salesforce.txt","w","utf-8")
    for person in people["records"]:
    

        name = person['Name']
        print "name = " + name

        emailid =  person['Email']
        print "email = " + emailid

        account = person['Account']['Name']
        print "account = " + account

        print "\n"
    
        
        name_in_email = str(emailid).split('@')[0]

        query_1 = "select Name, Email from User where  IsPortalEnabled=true and Email Like '" + name_in_email + '%'+ "'"
        result = sf.query(query_1)
   
        if result["totalSize"] == 1:

            print "\n"


            resultfile.write( name + "," + emailid + "," + account)
            resultfile.write("\n")

        time.sleep(1)

    resultfile.close()




search_in_salesforce()
