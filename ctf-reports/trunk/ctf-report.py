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
config.read('ctf-reports-config.txt')

log_file = 'logs/ctf-report-' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


report_file = 'logs/ctf-details-' + timestamp + '.txt'
report = open(report_file,'wb')



teamforge_folder = config.get('settings','teamforge-folder')


#get hostname
hostname = socket.gethostname()

report.write("hostname = " + hostname +"\n\n")

logging.info("\n" + "**********")
logging.info("hostname = " + hostname)

#get IP address
ipaddress = socket.gethostbyname(socket.gethostname())

report.write("IP address = " + ipaddress +"\n\n")
logging.info("IP address = " + ipaddress)







#running date
p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
#print "Today is", output
report.write(output +"\n\n")

logging.info(output)


platform_info = platform.dist()[0]
#print "Operating System is", platform_info
report.write("Operating System =" +  platform_info + "\n\n")
logging.info("Operating System =" +  platform_info)


#running df -h
folder = config.get('settings','data-mount-point')


size_command = "df | grep " + folder 

 


logging.info("running 'df ' command")
p = subprocess.Popen(size_command,shell=True, stdout=subprocess.PIPE)
size, err = p.communicate()

total_size = size.split()[0]
used_size = size.split()[1]
available_size = size.split()[2]
used_percentage = size.split()[3]


#print "*** Running 'df -h' command ***\n", total_size
report.write("Disk Space \n")
report.write("Total Size = ")
report.write(total_size + "\n")

report.write("Used Size = ")
report.write(used_size + "\n")

report.write("Available Size = ")
report.write(available_size + "\n")

report.write("Used Percentage = ")
report.write(used_percentage + "\n\n\n")





#running free -m
logging.info("running 'free -m' command")
p = subprocess.Popen(["free", "-m"], stdout=subprocess.PIPE)
memory, err = p.communicate()
#print "*** Running 'free -m' command ***\n", memory
report.write("*** Free Memory ***\n")
report.write(memory + "\n\n")


#get RAM size

proc = open('/proc/meminfo').readlines()
total_ram = proc[0].split()[1]




#running lscpu
logging.info("running 'lscpu' command")
p = subprocess.Popen(["lscpu | head -4"], stdout=subprocess.PIPE,shell=True)
cpuinfo, err = p.communicate()
#print "*** Running 'lscpu' command ***\n", cpuinfo
report.write("*** CPU details ***\n")
report.write(cpuinfo + "\n\n")




#count svn repos

svnroot = config.get('settings','svnroot')
#print svnroot

command = "ls  " +  svnroot + "/ | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
svn_repo_count, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", svn_repo_count
#report.write("*** ***\n")
report.write("No of SVN repositories at " + svnroot + " = " + str(int(svn_repo_count)-1) + "\n")

#report.write(output + "\n\n")




#calculating size for svnroot
command = "du -s " + svnroot + "/ |awk '{print $1}'"
#print command
logging.info("running 'du -s --max-depth=1 svnroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
svn_repo_size, err = p.communicate()
#print "*** Running 'du -s  svnroot' command ***\n", svn_repo_size
report.write("Size of SVN Repositories = ")
report.write(svn_repo_size + "\n\n")




#calculating size for svm_archieve
command = "du -s " + teamforge_folder  + "/var/scm-archive" + "|awk '{print $1}'"
#print command
logging.info("running 'du -s --max-depth=1 svnroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
deleted_svn_repo_size, err = p.communicate()
#print "*** Running 'du -s  var/scm-archive' command ***\n", deleted_svn_repo_size
report.write("Size of Deleted SVN Repositories = ")
report.write(deleted_svn_repo_size + "\n\n")


total_svn_repo_size = int(svn_repo_size) + int(deleted_svn_repo_size)
#print "total = " , total_svn_repo_size
#sys.exit()

#count git repos

gitroot = config.get('settings','gitroot')
#print gitroot

command = "ls  " +  gitroot + "/ | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
git_repo_count, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", git_repo_count
#report.write("*** ***\n")
report.write("No of git repositories at " + gitroot + " = " + str(int(git_repo_count)-1) + "\n")





#calculating size for gitroot
command = "du -s  " + gitroot + "/ |awk '{print $1}'"
#print command
logging.info("running 'du -s  gitroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
git_repo_size, err = p.communicate()
#print "*** Running 'du -s gitroot' command ***\n", git_repo_size
report.write("Size of git Repositories = ")
report.write(git_repo_size + "\n\n")






#count cvs repos

cvsroot = config.get('settings','cvsroot')
#print cvsroot

command = "ls " +  cvsroot + "/ | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
cvs_repo_count, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", cvs_repo_count
#report.write("*** ***\n")
report.write("No of cvs repositories at " + cvsroot + " = " + str(int(cvs_repo_count)-1) + "\n")





#calculating size for cvsroot
command = "du -s " + cvsroot + "/ |awk '{print $1}'"
#print command
logging.info("running 'du -s  cvsroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
cvs_repo_size, err = p.communicate()
#print "*** Running 'du -s  cvsroot' command ***\n", cvs_repo_size
report.write("Size of cvs Repositories = ")
report.write(cvs_repo_size + "\n\n")



total_repo_count = (int(svn_repo_count) + int(git_repo_count) + int(cvs_repo_count))-3


#find CTF version

teamforge_folder = config.get('settings','teamforge-folder')

command = "cat " + teamforge_folder + "/dist/version/core-version.txt | head -1 |  awk -F '=' '{print $2}' "
#print command
logging.info("running "+ "'" + command + "'" +" command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
ctf_version, err = p.communicate()
#print "***running "+ "'" + command + "'" +" command ***\n", ctf_version
report.write("CollabNet TeamForge Version = ")
report.write(ctf_version + "\n\n")



#find Real Host Name and blackduck availability

runtime_options = open(teamforge_folder + "/runtime/conf/runtime-options.conf","r")

blackduck_status = "Not Available"	

for line in runtime_options:
	if re.match("APPSERVER_DOMAIN", line):
		real_hostname = line.split('=')[1]
	
	if re.match("BDCS_HOST=", line):
		blackduck_status = "Available"



#print "Hostname = " + real_hostname
report.write("Real Hostname = ")
report.write(real_hostname + "\n\n")



#print "Blackduck Status " + blackduck_status
report.write("Blackduck Status = ")
report.write(blackduck_status + "\n\n")

runtime_options.close()



#find no of license

sflicense = open(teamforge_folder + "/var/etc/sflicense.txt")

for line in sflicense:
	if "ALM" in line:
		ALM = line.split(":")[0]
		SCM = line.split(":")[1]
		license = ALM + " : " + SCM
	else:
		license = line.split(":")[0]
		break	


#print "No of License " + license
report.write("No of License = ")
report.write(license + "\n\n")

sflicense.close()



#find no of artifacts

command = "echo 'select count(*) from artifact;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_artifacts, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_artifacts
#report.write("*** ***\n")
report.write("No of artifacts  = " + str(int(no_of_artifacts)) + "\n\n")


#find no of users

command = "echo " + " \"select count(*) from sfuser where is_deleted = 'f' AND status != 'Removed' ;\" " +" |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_users, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_users
#report.write("*** ***\n")


# Deducting 4 system users from the users count

no_of_users = int(no_of_users) - 4

report.write("No of Users  = " + str(no_of_users) + "\n\n")








#find no of Projects

command = "echo 'select count(*) from project;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_projects, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_projects
#report.write("*** ***\n")
report.write("No of Projects  = " + str(int(no_of_projects)) + "\n\n")



#find no of Documents

command = "echo 'select count(*) from document;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_documents, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_documents
#report.write("*** ***\n")
report.write("No of Documents  = " + str(int(no_of_documents)) + "\n\n")







#find no of active users in last 30 days

command = "echo " +  " \"select count(distinct(created_by_id)) from audit_entry where date_created <= now() and date_created >= now() - INTERVAL '30 DAYS';\" " + " |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_active_users_in_30_days, err = p.communicate()
#print "*** Running " + "'" + command + "'" + " command ***\n", no_of_active_users_in_30_days
#report.write("*** ***\n")
report.write("No of Active users in last 30 days  = " + str(int(no_of_active_users_in_30_days)) + "\n\n")

report.close()





salesforce_username = config.get('settings','salesforce_username')
salesforce_password = config.get('settings','salesforce_password')
salesforce_security_token = config.get('settings','salesforce_security_token')


try:
	sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)

except:
	logging.info("Error connecting to salesforce. Check Username, password and security token in ctf-reports-config.txt")
	sys.exit(1)

real_hostname = real_hostname.rstrip()

find_account_page_query = "SELECT Id FROM Account WHERE Domain_Name__c LIKE " + "'%" + real_hostname + "%'"
#print find_account_page_query
account_object = sf.query(find_account_page_query)

#print account_object

account_id = account_object["records"][0]['Id']

#print "Updating Salesforce Account"


server_details = "Available RAM = " + total_ram + " kb  \n" + cpuinfo


#reportfile = open(report_file,'r')
#ctf_server_details = reportfile.read()
#reportfile.close()



#print ctf_version
          
         
sf.Server_stats__c.create(
        {'Account__c':account_id,
        'Total_Projects__c':no_of_projects,
        'Active_Projects__c':0,
        'Disk_utilization_for_Git_Repos__c':git_repo_size,
        'Total_Git_Repos__c':git_repo_count,
        'Bandwidth__c': 0,
        'Server_Description__c':server_details,
        'Total_Licenses_issued__c':license,
        'Total_Licenses_Activated__c':no_of_users,
        'Active_Users__c':no_of_active_users_in_30_days,
        'Disk_utilization_for_SVN_Repos__c':total_svn_repo_size,
        'Total_SVN_Repos__c':svn_repo_count, 
        'Current_Release__c':ctf_version,
    	'Total_Disk_Utilization__c':used_size } )
	    








#print "done"



 
