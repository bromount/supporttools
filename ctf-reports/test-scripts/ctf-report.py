import subprocess
import logging
import ConfigParser
import socket
import re
from simple_salesforce import Salesforce
import platform

config = ConfigParser.ConfigParser()
config.read('ctf-reports-config.txt')

logging.basicConfig(filename="ctf-reports.log", level=logging.INFO)


report = open('ctf-details.txt','wb')


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
print "Today is", output
report.write(output +"\n\n")

logging.info(output)


platform_info = platform.platform()
print "Operating System is", platform_info
report.write("Operating System =" +  platform_info + "\n\n")
logging.info("Operating System =" +  platform_info)


#running df -h
folder = config.get('settings','data-mount-point')


size_command = "df | grep " + folder 

 


logging.info("running 'df ' command")
p = subprocess.Popen(size_command,shell=True, stdout=subprocess.PIPE)
size, err = p.communicate()

total_size = size.split()[1]
used_size = size.split()[2]
available_size = size.split()[3]
used_percentage = size.split()[4]


print "*** Running 'df -h' command ***\n", total_size
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
#logging.info("running 'free -m' command")
#p = subprocess.Popen(["free", "-m"], stdout=subprocess.PIPE)
#output, err = p.communicate()
#print "*** Running 'free -m' command ***\n", output
#report.write("*** Free Memory ***\n")
#report.write(output + "\n\n")



#count svn repos

svnroot = config.get('settings','svnroot')
print svnroot

command = "ls -lh " +  svnroot + " | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
svn_repo_count, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", svn_repo_count
#report.write("*** ***\n")
report.write("No of SVN repositories at " + svnroot + " = " + str(int(svn_repo_count)-1) + "\n")

#report.write(output + "\n\n")




#calculating size for svnroot
command = "du -sh " + svnroot + "|awk '{print $1}'"
print command
logging.info("running 'u -h --max-depth=1 svnroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
svn_repo_size, err = p.communicate()
print "*** Running 'du -sh  svnroot' command ***\n", svn_repo_size
report.write("Size of SVN Repositories = ")
report.write(svn_repo_size + "\n\n")




#count git repos

gitroot = config.get('settings','gitroot')
print gitroot

command = "ls -lh " +  gitroot + " | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
git_repo_count, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", git_repo_count
#report.write("*** ***\n")
report.write("No of git repositories at " + gitroot + " = " + str(int(git_repo_count)-1) + "\n")





#calculating size for gitroot
command = "du -sh  " + gitroot + "|awk '{print $1}'"
print command
logging.info("running 'du -sh  gitroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
git_repo_size, err = p.communicate()
print "*** Running 'du -sh gitroot' command ***\n", git_repo_size
report.write("Size of git Repositories = ")
report.write(git_repo_size + "\n\n")






#count cvs repos

cvsroot = config.get('settings','cvsroot')
print cvsroot

command = "ls -lh " +  cvsroot + " | wc -l"



logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
cvs_repo_count, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", cvs_repo_count
#report.write("*** ***\n")
report.write("No of cvs repositories at " + cvsroot + " = " + str(int(cvs_repo_count)-1) + "\n")





#calculating size for cvsroot
command = "du -sh " + cvsroot + "|awk '{print $1}'"
print command
logging.info("running 'du -sh  cvsroot' command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
cvs_repo_size, err = p.communicate()
print "*** Running 'du -sh  cvsroot' command ***\n", cvs_repo_size
report.write("Size of cvs Repositories = ")
report.write(cvs_repo_size + "\n\n")



total_repo_count = (int(svn_repo_count) + int(git_repo_count) + int(cvs_repo_count))-3


#find CTF version

teamforge_folder = config.get('settings','teamforge-folder')

command = "cat " + teamforge_folder + "/dist/version/core-version.txt | head -1 |  awk -F '=' '{print $2}' "
print command
logging.info("running "+ "'" + command + "'" +" command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
ctf_version, err = p.communicate()
print "***running "+ "'" + command + "'" +" command ***\n", ctf_version
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



print "Hostname = " + real_hostname
report.write("Real Hostname = ")
report.write(real_hostname + "\n\n")



print "Blackduck Status " + blackduck_status
report.write("Blackduck Status = ")
report.write(blackduck_status + "\n\n")

runtime_options.close()



#find no of license

sflicense = open(teamforge_folder + "/var/etc/sflicense.txt")

for line in sflicense:
	license = line.split(":")[0]


print "No of License " + license
report.write("No of License = ")
report.write(license + "\n\n")

sflicense.close()



#find no of artifacts

command = "echo 'select count(*) from artifact;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_artifacts, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", no_of_artifacts
#report.write("*** ***\n")
report.write("No of artifacts  = " + str(int(no_of_artifacts)) + "\n\n")


#find no of users

command = "echo 'select count(*) from sfuser;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_users, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", no_of_users
#report.write("*** ***\n")
report.write("No of Users  = " + str(int(no_of_users)) + "\n\n")




#find no of Projects

command = "echo 'select count(*) from project;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_projects, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", no_of_projects
#report.write("*** ***\n")
report.write("No of Projects  = " + str(int(no_of_projects)) + "\n\n")



#find no of Documents

command = "echo 'select count(*) from document;' |" +   teamforge_folder + "/runtime/scripts/psql-wrapper  | sed -n 3p"


logging.info("running " + command + "command")
p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
no_of_documents, err = p.communicate()
print "*** Running " + "'" + command + "'" + " command ***\n", no_of_documents
#report.write("*** ***\n")
report.write("No of Documents  = " + str(int(no_of_documents)) + "\n\n")

report.close()





salesforce_username = config.get('settings','salesforce_username')
salesforce_password = config.get('settings','salesforce_password')
salesforce_security_token = config.get('settings','salesforce_security_token')



sf = Salesforce(username=salesforce_username, password=salesforce_password, security_token=salesforce_security_token, sandbox=True)

real_hostname = real_hostname.rstrip()

find_account_page_query = "SELECT Id FROM Account WHERE Domain_Name__c LIKE " + "'%" + real_hostname + "%'"
print find_account_page_query
account_object = sf.query(find_account_page_query)

print account_object

account_id = account_object["records"][0]['Id']

print used_size

sf.Account.update(account_id,{'Operating_System__c': platform_info})
sf.Account.update(account_id,{'Count_of_Artifacts__c': no_of_artifacts})
sf.Account.update(account_id,{'Count_of_Projects__c': no_of_projects})
sf.Account.update(account_id,{'Current_Release__c': ctf_version})
sf.Account.update(account_id,{'Disk_Usage__c': used_size})
sf.Account.update(account_id,{'Count_of_Repositories__c':total_repo_count})

print "done"



 
