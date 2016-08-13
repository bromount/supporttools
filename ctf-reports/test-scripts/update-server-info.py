
#sudo easy_install simple_salesforce
#https://github.com/neworganizing/simple-salesforce


from simple_salesforce import Salesforce
import simplejson
import json
#from simple_salesforce import SalesforceLogin

OS = "CentOS 6"

sf = Salesforce(username='shrinivasan@collab.net.fullcopyqa', password='w3lc0me', security_token='kOHKlAzXlACZVN39RiLft7HE', sandbox=True)
print sf
#session_id, sf = SalesforceLogin('shrinivasan@collab.net.fullcopyqa', 'w3lc0me', 'kOHKlAzXlACZVN39RiLft7HE', True)
#con = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})

#print con

acc = sf.Account.get('0013000000GgWwe')
#sf.Account.update('0013000000GgWwe',{'Operating_System__c': 'RedHat 6'})


result = sf.query("SELECT Id FROM Account WHERE Domain_Name__c = 'https://advadevnet.com/'")


account_id = result["records"][0]['Id']

sf.Account.update(account_id,{'Operating_System__c': OS})

print "done"

#result_json = result.read()
#    print r

#data = json.loads(result_json)
#print data

#parsed_data = simplejson.loads(result)
#id = parsed_data['id']
#print id
