#!/usr/bin/env python

# script to export set of files added/modified files in a given revision
# contact shrinivasan@collab.net for any queries



repo = raw_input( "Enter the Repository URL : ").strip()
revision = raw_input("Enter the revision no : ").strip()
username = raw_input("Enter the username : ").strip()

# touchpath = "/usr/bin/touch"
stack = ""
stack1 = ""


import subprocess
import os

#svn diff <repo> -c<version-no> --summarize
#will give the changeset of a repo in given version

print "Getting the changeset"

change = subprocess.Popen(["svn","diff",repo,"-c" + revision,"--summarize","--username",username],stdout=subprocess.PIPE)
changeset = change.communicate()[0]


print changeset
repository = repo[::-1]
repository = repository.split('/')
repository = repository[0]
repository = repository[::-1]


#This function checks for the path and using "svn info <path>" returns as file or folder
def find_property(path):
	prop = subprocess.Popen(["svn","info",path+"@"+revision,"--username",username],stdout=subprocess.PIPE)
	path_property = prop.communicate()[0]
	node_kind = path_property.splitlines()[6]
	return node_kind.split(":")[1].strip()

for line in changeset.splitlines():
	stack = ""		
        if line.strip():
                filename = line.split()
                fullpath =  filename[1].strip()
		prop = find_property(fullpath)
		filepath = fullpath.split(repo)
                eachnode = filepath[1].split('/')
                length = len(eachnode)-1
                for file in eachnode:
                        if file != '':
                        	if eachnode.index(file) == length:
					if stack == stack1:
	                                        if prop == 'file':
							change = "cd " + repository + "/" + stack + ";"
	                                                filled = change + "svn export -r " + revision +" "+ fullpath+ "@" + revision + " --username " + username
	                                                f = os.popen(filled)
							f.read()
							print "Exported " +repository + "/" + stack + file
	                                        else:
	                                                print "Creating Directories"
							directory = "mkdir " + repository + "/" + stack + file
	                                                os.popen(directory)

					else:
	                                        if prop == 'file': 
							directory = "mkdir -p " + repository + "/" + stack
							os.popen(directory)
							change = "cd " + repository + "/" + stack + ";"
       	                                		filled = change + "svn export -r " + revision + " " + fullpath + "@" + revision + " --username " + username
       	                                		f = os.popen(filled)
							f.read()
							print "Exported " + repository + "/" +stack + file
						else:
							print "Creating Directories"
							directory = "mkdir -p " + repository + "/" + stack + file
							os.popen(directory)
               	                else:
					stack = stack +file + "/"
	stack1 = stack 



print "Done"
