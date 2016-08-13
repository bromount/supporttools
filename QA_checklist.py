#!/usr/bin/env python
# attempts to impliment the QA checklist 
# (https://forge.collab.net/svn/repos/support/CTF_Hosted_checklist.txt)
# via the SOAP API

if __name__ == '__main__':
    from SOAPpy import WSDL
    import SOAPpy
    import sys
    import pprint
    import array

    hostname = 'ctf53'
    username = 'admin'
    password = 'admin'

    testusername = 'test'

    # get necassary WSDLs
    CollabNetWSDL= 'http://'+hostname+'/ce-soap50/services/CollabNet?wsdl'
    FrsWSDL = 'http://'+hostname+'/ce-soap50/services/FrsApp?wsdl'
    RbacWSDL = 'http://'+hostname+'/ce-soap50/services/RbacApp?wsdl'
    try:
        collabnet = WSDL.SOAPProxy(CollabNetWSDL)
        frs = WSDL.SOAPProxy(FrsWSDL)
	rbac = WSDL.SOAPProxy(RbacWSDL)
    except:
        print "Hrmms.  Grabbing the WSDL file failed"
        sys.exit(1)

    # admin login
    try:
        admin_session = collabnet.login(username,password)
    except:
        print "Unable to login as %s" % username
        sys.exit(1)

## Project creation    
    print "Creating test project...\t",
    try:
        project = collabnet.createProject(admin_session,'','Test Project','Test Project')
    except SOAPpy.faultType, fault:
        print "Failed - ",
	print fault['detail']['exceptionName']
	print "Cannot continue without a test project."
	sys.exit(1)
    else:
	print "Passed"	

## User creation
#    print "Creating test user..\t\t",
#    try:
#        testuser = collabnet.createUser(admin_session, testusername,'devnull@collab.net','Test User','en','EST',False,False,'password')    
#    except SOAPpy.faultType, fault:
#        print "Failed - ",
#        print fault['detail']['exceptionName']
#	print "Cannot continue without a test user."
#	sys.exit(1)
#    else:
#	print "Passed"	 

       
## Rbac
    try:	
        print "Creating test role...\t\t",
        role = rbac.createRole(admin_session,project['id'],'test','testing role')
        print "Passed"
	
	print "Adding testuser to role...\t",
        rbac.addUser(admin_session,role['id'],testusername)
        print "Passed"        
        print "Adding FRS perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'frs_create','')
	print "Passed"
	print "Adding Wiki perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'wiki_create','')
	print "Passed"
	print "Adding Discussion perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'discussion_participate','')
	print "Passed"
	print "Adding Docman perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'docman_create','')
	print "Passed"
	print "adding Project Page perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'html_edit','')
	print "Passed"
	print "Adding Tracker perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'tracker_create','')
	print "Passed"
	print "Adding Task perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'taskmgr_create','')
	print "Passed"
	print "Adding SCM perms to role...\t",
        rbac.addCluster(admin_session,role['id'],'scm_commit','')
	print "Passed"

	print "Adding test user to project..\t",
        collabnet.addProjectMember(admin_session,project['id'],testusername)
        print "Passed"
 
    except SOAPpy.faultType, fault:
        print "Failed - ",
        print fault['detail']['exceptionName']
    else:
        print "All test passed"

#    print "Logging in as test user..\t",
#    try:
#        test_session = collabnet.login(testusername,'password')    
#	print "Passed"

    # del project after run to make testing easier
    #collabnet.deleteProject(admin_session, project['id'])

    # logout
    logout = collabnet.logoff(username,admin_session)
#    logout = collabnet.logoff(testusername,test_session)
