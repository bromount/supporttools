import mechanize
import cookielib
import re
from bs4 import BeautifulSoup


class cee:
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    loginusername = ''
    password = ''

    username = ''
    email = ''
    realname = ''
    organization = ''
    firstname = ''
    lastname = ''
    product = ''
    revenue = ''
    role = ''
    state = ''
    country = ''

    new_email = ''
    new_organization = ''
    new_firstname = ''
    new_lastname = ''
    new_revenue = ''
    new_role = ''
    new_state = ''
    new_country = ''



    def login(self):

        # The site we will navigate into, handling it's session
        self.br.open('http://www.open.collab.net/servlets/Login?detour=http://www.collab.net/')

        # Select the first (index zero) form
        self.br.select_form(nr=1)

        # User credentials
        self.br.form['loginID'] = self.loginusername
        self.br.form['password'] = self.password

        # Login
        self.br.submit()


    def create_user(self):

        self.br.open('http://www.open.collab.net/servlets/UserAdd')

        self.br.select_form(nr=1)

        self.br.form['userName'] = self.username

        self.br.form['email'] = self.email

        self.br.form['realName'] = self.realname

        self.br.form['organization'] = self.organization

        self.br.form['SET-ATTRIBUTE helm ocnFirstName 2 Y'] = self.firstname

        self.br.form['SET-ATTRIBUTE helm ocnLastName 2 Y'] = self.lastname

        self.br.form['ATTRIBUTE helm ocnProduct 2 Y'] = self.product

        self.br.form['SET-ATTRIBUTE helm ocnCompanyRevenue 2 Y'] = self.revenue

        self.br.form['SET-ATTRIBUTE helm ocnRole2 2 Y'] = self.role

        self.br.form['SET-ATTRIBUTE helm ocnState 2 Y'] = self.state

        self.br.form['SET-ATTRIBUTE helm ocnCountry 2 Y'] = self.country

        self.br.submit()

        print self.br


    def delete_user(self,username):
        self.br.self.br.open('http://www.open.collab.net/servlets/UserDelete')

        self.br.select_form(nr=1)

        self.br.form['massDelete'] = username

        self.br.submit()

        self.br.select_form(nr=1)

        self.br.submit()
        print "user " + username + "deleted"





    def search_user(self,email):

        self.result = self.br.open('http://www.open.collab.net/servlets/UserList')

        self.br.select_form(nr=1)

        self.br.form['field'] = ['EmailAddress']

        self.br.form['matchType'] = ['contains']

        self.br.form['matchValue'] = email

        self.br.submit()

	self.page = self.br.response()
	self.html = self.page.read()

	self.soup = BeautifulSoup(self.html)
	#print soup.prettify()
	
	self.table = self.soup.find("table",width="100%")
	#print self.table
	
	
	self.rows = self.soup.find_all('tr', {'class': re.compile('a')})
	
	if self.rows:
	  for self.row in self.rows:
	      #print self.row
	      self.cols = self.row.findAll('td')
	      #print self.cols
	      self.existing_username = self.cols[0].text.strip()
	      self.existing_email = self.cols[1].text.strip()
	      self.existing_organization = self.cols[2].text.strip()
	      
	      self.result=[self.existing_username ,self.existing_email,self.existing_organization]
	      print self.existing_username 
	      print self.existing_email
	      print self.existing_organization
#	return self.result
        else:
	     self.existing_username = ""
	     self.existing_email = ""
	     self.existing_organization = ""
	
        #for link in self.br.links():
##            print link
	    
            #LinkMatch = re.compile( 'UserEdit' ).search( link.url )

	
	    #if  LinkMatch:
		  #print link.url
##            if LinkMatch in link:
##                print link

	  
