import cee
import csv
import logging
import time
import datetime
import ConfigParser
import os

dir = os.path.dirname(__file__)
sw_users_in_salesforce = os.path.join(dir, 'data/scrumworks-users-in-salesforce.txt')

config = ConfigParser.ConfigParser()
config.read('config.txt')



ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

log_file = 'logs/search_ocn' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


ocn_username = config.get('settings','ocn_username')
ocn_password = config.get('settings','ocn_password')

def search_in_ocn():

    ocn = cee.cee()

    ocn.loginusername = ocn_username
    ocn.password = ocn_password
    print "Logging in to OCN"

    ocn.login()

    logging.info("Logged in OCN ")

    print ocn

    print "Connected to OCN"

    miss = open("missing_contacts_in_ocn.csv","w")

    with open(sw_users_in_salesforce, 'r') as f:
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


    miss.close()

if "__main__"=="__main__":
    search_in_ocn()
               
                        
                            


            

