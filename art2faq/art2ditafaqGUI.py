#!/usr/bin/env python
#
# $URL: https://forge.collab.net/svn/repos/supporttools/art2faq/art2ditafaqGUI.py $
# $Id: art2ditafaqGUI.py 33 2009-12-12 00:25:17Z jdickison $
# $Date: 2009-12-12 05:55:17 +0530 (Sat, 12 Dec 2009) $
# $Author: jdickison $
#

import wx
import sys
import os
import string
import csv

def dirchoose():
    'Gives the user selected path. Use: dirchoose()'
    global _selectedDir , _userCancel #you should define them before
    userPath = 'c:/'
    app = wx.App()
    dialog = wx.DirDialog(None, "Please choose your project directory:",\
    style=1 ,defaultPath=userPath, pos = (10,10))
    if dialog.ShowModal() == wx.ID_OK:
        _selectedDir = dialog.GetPath()
        print _selectedDir
        return _selectedDir
    else:
        #app.Close()
        dialog.Destroy()
        return _userCancel

def filechoose():
    'Gives the user selected path. Use: dirchoose()'
    global _selectedFile , _userCancel #you should define them before
    userPath = 'c:/'
    app = wx.App()
    dialog = wx.FileDialog(None, "Please choose your project File:",style = wx.OPEN )
    if dialog.ShowModal() == wx.ID_OK:
        print 'Selected:', dialog.GetPath()
        _selectedFile = dialog.GetPath()
        return _selectedFile

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

if __name__ == "__main__":
    rownum=0
    OutputDir = dirchoose()
    InFile = filechoose()
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


