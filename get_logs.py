#!/opt/collabnet/teamforge//runtime/bin/wrapper/python
import getopt,sys,datetime,tarfile,os,smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

import app.util


def usage():
    print " usage: get_logs.py [-h] [-t, --type {app,scm,mail,all}] [-d, --date DATE]"
    print "     [-s, --string STRING]\n"
    print "Gather CTF logs.\n"
    print "optional arguments:"
    print "  -h, --help    \tshow this help message and exit"
    print "  -t, --type {app,scm,mail,all}\n\t\t\tType of logs to get."
    print "  -d, --date YYYY/MM/DD\tDate of logs to get."
    print "  -s, --string STRING\tGet logs containing STRING"
    print "  -f, --file FILE\tSave compressed logs to FILE"
    print "  -e, --email user@domain\tIf set to users email address, will send logs via email to Support"

def get_logs(outfile, type, date, string):
    ctf_cfg = app.util.getRuntimeConfiguration()

    # default to all logs
    dir = ctf_cfg.get('LOG_DIR')
    
    # set dir based on log type
    if type == 'app':
        dir = ctf_cfg.get('APPLICATION_LOG_DIR')
    elif type == 'scm':
        dir = ctf_cfg.get('INTEGRATION_LOG_DIR')
    elif type == 'mail':
        dir = ctf_cfg.get('JAMES_LOG_DIR')

    print "Gathering logs. Please be paient..."
    
    # get list of files in dir
    files = list()
    for path, dirlist, filelist in os.walk(dir):
        os.chdir(path)
        for file in filelist:
            files.append(os.path.abspath(file))
        
    # if date is set, filter list by date
    if date != '':
        files = logsby_date(files, date)
    # if string is set, check for string in file
    if string != '':
        files = search_logs(string, files)

    if not files:
        print "No files found!"
        sys.exit(2)

    print "Writing", len(files),  "logs to",outfile

    # create tgz outfile with list files
    tar = tarfile.open(outfile, "w|gz")
    # add files to tar
    for file in files:
        tar.add(file)
    tar.close()

# accepts a list of files and date
# returns a list of files    	
def logsby_date(files, date):
    matches = list() 
    for file in files:
        # if date is set, compare with ctime of file
        if date != '':
            if date == date.fromtimestamp(os.path.getctime(file)):
                matches.append(file)
    return matches

# accepts string to search for and list of files
# return list of matches
def search_logs(string, files):

    matches = list()
    for file in files:
        infile = open(file, "r")
        text = infile.read()
        infile.close()
        if text.find(string) == 0:
            matches.append(file)
    return matches


def email_logs(email, outfile):
    case_email = 'cnsupport@collab.net'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = case_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "CTF error"
    
    msg.attach( MIMEText("A CTF error occured, pleae find the logs attached") )
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(outfile,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(outfile))
    msg.attach(part)
   
    print "Sending logs via email..." 
    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(email, case_email, msg.as_string())
    smtp.close() 
 
def main():
    # set some defaults
    type = 'all'
    date = ''
    string = ''
    outfile = '/tmp/logs.tgz'
    email = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:d:s:f:e:", ["help", "type", "date", "string", "file", "email"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for opt, val in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-t", "--type"):
            if val in ("app", "scm", "mail", "all"):
                type = val
            else:
                print "Unknown type.\n"
                usage()
                sys.exit(2)
        elif opt in ("-s", "--string"):
            string = val
        elif opt in ("-d", "--date"):
            date = val.rsplit('/')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        elif opt in ("-f", "--file"):
            outfile = val
        elif opt in ("-e", "--email"):
            email = val    
        else:
            assert False, "unhandled option"

    get_logs(outfile, type, date, string)

    if email != '':
        email_logs(email, outfile)

if __name__ == "__main__":
    main()

