#!/usr/bin/env python 
# $URL: https://forge.collab.net/svn/repos/supporttools/art2faq/art2ditafaq.py $
# $Id: art2ditafaq.py 31 2009-12-11 19:33:17Z jdickison $
# $Date: 2009-12-12 01:03:17 +0530 (Sat, 12 Dec 2009) $
# $Author: jdickison $

import sys
import os
import string
import csv
import getopt
options, args = getopt.getopt(sys.argv[1:], 'o:i:h',
        ['output=', 'input=']
         )

def usage():
    print "usage: ",sys.argv[0]," -o -i   All options are required to run"
    print "-o : output dir"
    print "-i : input file"

def parseopts():
    options, args = getopt.getopt(sys.argv[1:], 'o:i:h',
        ['output=', 'input=']
         )
    if len(options) < 1:
        usage(); print "foo";sys.exit(0)
    opts = {}
    for o, a in options:
        opts[o] = a
    if '-h' in opts or '--help' in opts:
        usage(); print "found h"; sys.exit(0)
    if '-o' in opts:
        OutputDir=opts['-o']
        if not os.path.exists(OutputDir):
            print "dest %s does not exitst, making it" %OutputDir
            if not OutputDir[len(OutputDir)-1] == "/":
                OutputDir=OutputDir+"/"
            os.makedirs(OutputDir)
    if '-i' in opts:
        InFile=opts['-i'] 
        print InFile
    if not '-i' in opts:
        usage(); print "no -i givien" ; sys.exit(0)
    if not '-o' in opts:
        usage(); print "no -o given " ;sys.exit(0)
    return OutputDir,InFile

def procCsv(myrow):
    print "*" * 80 
    extList = [".xml"]
    #print myrow
    if not myrow: return
    ConID=row[0]
    Title=row[1]
    ShortDesc=row[2]
    ConBody=row[18]
    FileName=row[13]
    #print ConID 
    if FileName == 'tbd':
        FileName=row[0]+".xml"
    if FileName == 'NA':
        FileName=row[0]+".xml"
    if not os.path.splitext(FileName)[1] in extList:
        FileName=FileName=ConID+".xml"
    if not FileName:
        #FileName='rename-me-artifaq'+str(random.randint(1, 10))+".xml"
        FileName=row[0]+".xml"
    if FileName == '.xml':
        #FileName='rename-me-artifaq'+str(random.randint(1, 10))+".xml"
        FileName=row[0]+".xml"
    FileName=string.replace(FileName, '/','_')
    FileName=string.replace(FileName, '\\','_')
    #print FileName
    xml ='''<?xml version="1.0" encoding="utf-8"?>
            <!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" 
            "http://docs.oasis-open.org/dita/v1.1/OS/dtd/concept.dtd">
            <concept id="%s" xml:lang="en-us">
            <title>%s</title>
            <shortdesc>%s</shortdesc>
            <conbody>%s
            <p></p>
            <!--        <section>
            <title>Version</title>
            <p>5.3</p>
            </section>-->
            </conbody>
            <!--  <related-links>
            <link href="http:// " format="html" scope="external">
            <linktext> </linktext>
            </link>
            </related-links>  -->
            <!-- <xref
            href="http://" format="html" scope="external">
            (ink text here)
            </xref> -->
            <!-- <ph audience="internal">(issue 39881)</ph> -->
            </concept>
        ''' % (ConID,Title,ShortDesc,ConBody)
    return xml,FileName

if __name__ == '__main__':
    options, args = getopt.getopt(sys.argv[1:], 'o:i:h',
        ['output=', 'input=']
         )

    rownum=0
    OutputDir,InFile=parseopts()
    ifile  = open(InFile, "rb")
    reader = csv.reader(ifile)
    for row in reader:
        if rownum == 0:
            header = row
            rownum += 1
        else:
            if not row: break
            OutFile,FileName=procCsv(row)
            X = string.replace(OutFile, '\r', '' )
            FILE = open(OutputDir+FileName,"w")
            print "Writing %s" %OutputDir+FileName
            FILE.writelines(X)
        
    print "all done"
