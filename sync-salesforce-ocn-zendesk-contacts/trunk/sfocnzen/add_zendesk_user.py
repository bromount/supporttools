#!/usr/bin/python
# -*- coding: utf-8 -*-

#script to add organization and users

#provide all required information at config.txt


import ConfigParser
import time
import datetime
import logging
import cee
import csv
import sys
import urllib2
import base64
import json 


config = ConfigParser.ConfigParser()
config.read('config.txt')

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

log_file = 'logs/add_zendesk_user_' + timestamp + '.log'
logging.basicConfig(filename=log_file, level=logging.INFO)


zen_username = config.get('settings','zendesk_username')
zen_password = config.get('settings','zendesk_password')
zen_sitename = config.get('settings','zendesk_sitename')


def sync_zendesk_user():

    with open('data/missing_contacts_in_ocn.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            
            time.sleep(1)

            sf_name = row[0].strip()
            sf_email = row[1].strip()
            sf_organization = row[2].strip()


            url = zen_sitename + '/api/v2/users/search.json?query=' + sf_email

          #  print url
            
            req = urllib2.Request(url= url,  headers={'Content-Type': 'application/json'})
            base64string = base64.encodestring('%s:%s' % (zen_username,zen_password)).replace('\n','')
            req.add_header("Authorization","Basic %s" % base64string)
            result = urllib2.urlopen(req)

            result_json = result.read()

            print result_json

            data = json.loads(result_json)

            user_count = data['count']
            print user_count
            
             
            if user_count > 0:
                user_id = data['users'][0]['id']
                print user_id
                                
                data = {"user": {"tags": ["paying"]}}
                jsondata = json.dumps(data)
                user_edit_url = zen_sitename + '/api/v2/users/' + str(user_id) + '.json'
                print user_edit_url
                logging.info("Adding Paying tag to user " + user_edit_url)

                req = urllib2.Request(url=user_edit_url, data = jsondata, headers={'Content-Type': 'application/json'})
                base64string = base64.encodestring('%s:%s' % (zen_username,zen_password)).replace('\n','')
                req.add_header("Authorization","Basic %s" % base64string)
                req.get_method = lambda: 'PUT'
                
                try:
                    result = urllib2.urlopen(req)
                except Exception, err:
                    print traceback.format_exc()


            

sync_zendesk_user()                
