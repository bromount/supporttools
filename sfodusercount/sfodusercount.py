#!/usr/bin/env python
if __name__ == '__main__':
    from SOAPpy import WSDL
    import sys
    import smtplib
    import pprint
    import array
    import re

    hostname = 'ondemand.sourceforge.com'
    username = 'dthomas'
    password = 'w1llyb0b'

    smtpserver = 'localhost'
    RECIPIENTS = ['eoberthier@collab.net']
    SENDER = 'forge@support.extranet.collab.net'
    message = 'From: SFOD Admins <forge@support.extranet.collab.net>\nSubject: Project membership on SFOD\n\n'

    pattern = re.compile('.* - Support.*')
    
    SourceForgeWSDL= 'https://'+hostname+'/sf-soap44/services/SourceForge?wsdl'
    try:
        sourceforge = WSDL.Proxy(SourceForgeWSDL)
    except:
        print "Hrmms.  Grabbing the WSDL file at %s failed." % wsdlFile
        sys.exit(1)
    loginhash = sourceforge.login(username,password)
    projectlist = sourceforge.getProjectList(loginhash)
    for project in projectlist['dataRows']:
        projectmemberlist = sourceforge.getProjectMemberList(loginhash,project['id'])
        if not pattern.match(project['title']):
                #print "%s - %s members" % (project['title'], len(projectmemberlist['dataRows']))
                message = message + "%s - %s members\n" % (project['title'], len(projectmemberlist['dataRows']))
		for member in projectmemberlist['dataRows']:
			message = message + "\t%s\n" % (member['userName'])

    logout = sourceforge.logoff(username,loginhash)

    smtpsession = smtplib.SMTP(smtpserver)
    if smtpsession.sendmail(SENDER, RECIPIENTS, message.encode("utf-8")):
       print "Failed to send message"
    #print message
