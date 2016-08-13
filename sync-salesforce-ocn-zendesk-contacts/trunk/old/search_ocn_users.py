import cee
import csv
import logging
import time
import datetime

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

log_file = 'logs/search-' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


ocn = cee.cee()

ocn.loginusername = 'shrinivasan@collab.net'
ocn.password = 'l33ter'

ocn.login()

logging.info("Logged in OCN ")


print ocn

miss = open("miss.csv","w")

with open('scrumworks-contacts.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        
        time.sleep(1)

        sf_name = row[0].strip()
        sf_email = row[1].strip()
        sf_organization = row[2].strip()


        logging.info("Searching for email " + sf_email)

#        email = 'jeanie.conner@laserfiche.comd'
        ocn.search_user(sf_email)
#        print search_result

        if  ocn.existing_email:

            print "Found" + sf_email
#                       print search_result
#            for i in search_result:
#                  print i
    
#            print search_result[0]
#            print search_result[1]
#            print search_result[2]
#            print "============== \n"

            logging.info("Found email " + sf_email )
        else:
            print "Email not Found " + sf_email
            logging.info("Email not Found " + sf_email)
            miss.write(sf_name + "," + sf_email + "," + sf_organization)
            miss.write("\n")
