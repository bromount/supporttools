import ConfigParser
import time
import datetime
import logging
import cee
import csv
import sys


config = ConfigParser.ConfigParser()
config.read('config.txt')

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

log_file = 'logs/ocn_add_user_' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)

ocn_username = config.get('settings','ocn_username')
ocn_password = config.get('settings','ocn_password')

ocn = cee.cee()

ocn.loginusername = ocn_username
ocn.password = ocn_password

ocn.login()






def create_user_in_ocn(email,realname,organization,firstname,lastname):

    ocn.username = email

    ocn.email = email
    ocn.realname = realname
    ocn.organization = organization
    ocn.firstname = firstname
    ocn.lastname = lastname
    ocn.product = ['Cloud']
    ocn.revenue = ['888888']
    ocn.role = ['CEO']
    ocn.state = ['Alaska']
    ocn.country = ['US']


    #ocn.create_user()
    print ocn


#ocn.new_organization = "CollabNet1"
#ocn.edit_user('shrini')


def create_ocn_users():

    with open('data/missing_contacts_in_ocn.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            
            time.sleep(1)

            try:
                sf_name = row[0].strip()
                sf_email = row[1].strip()
                sf_organization = row[2].strip()
                sf_firstname = sf_name.split(' ')[0]
                sf_lastname = sf_name.split(' ')[-1]
                
                create_user_in_ocn(sf_email,sf_name,sf_organization,sf_firstname,sf_lastname)
                
                logging.info("adding user  " + sf_name + " ,  "  + sf_email )
                print "adding user  " + sf_name + " ,  "  + sf_email

            except:
                print "Unexpected error:", sys.exc_info()
                logging.exception('')
            
            
                



#if "__main__"=="__main__":
#    create_user_in_ocn()



