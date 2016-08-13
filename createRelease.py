#!/usr/bin/env python
# creates number of releases in num_rel in speficied pkg
# releases are named "1-N.x"

if __name__ == '__main__':
    from SOAPpy import WSDL
    import sys
    import pprint
    import array
    import re

    hostname = 'ctf52'
    username = 'admin'
    password = 'admin'
    num_rel = 10
    pkg = 'pkg1001'

    SourceForgeWSDL= 'http://'+hostname+'/sf-soap44/services/SourceForge?wsdl'
    FrsWSDL = 'http://'+hostname+'/sf-soap44/services/FrsApp?wsdl'
    try:
        sourceforge = WSDL.Proxy(SourceForgeWSDL)
        frs = WSDL.Proxy(FrsWSDL)

    except:
        print "Hrmms.  Grabbing the WSDL file failed"
        sys.exit(1)
    loginhash = sourceforge.login(username,password)
    
    for i in range(1, num_rel+1):
      rel = `i` + '.x'
      print "creating release: %s" % rel
      frs.createRelease(loginhash,pkg,rel,'description','active','General Availability');

    logout = sourceforge.logoff(username,loginhash)

