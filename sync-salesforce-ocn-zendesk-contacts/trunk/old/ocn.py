import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup


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

# The site we will navigate into, handling it's session
br.open('http://www.open.collab.net/servlets/Login?detour=http://www.collab.net/')

# Select the first (index zero) form
br.select_form(nr=1)

# User credentials
br.form['loginID'] = 'shrinivasan@collab.net'
br.form['password'] = 'l33ter'

# Login
br.submit()

br.open('http://www.open.collab.net/servlets/UserAdd')

br.select_form(nr=1)

#br.form['associatedProject'] = ['2']

br.form['userName'] = 'nithyadurai87'

br.form['email'] = 'nithyadurai87@gmail.com'

br.form['realName'] = 'Nithya Shrinivasan'

br.form['organization'] = 'Cognizant'

br.form['SET-ATTRIBUTE helm ocnFirstName 2 Y'] = 'Nithya'

br.form['SET-ATTRIBUTE helm ocnLastName 2 Y'] = 'Shrinivasan'

br.form['ATTRIBUTE helm ocnProduct 2 Y'] = ['Cloud']

br.form['SET-ATTRIBUTE helm ocnCompanyRevenue 2 Y'] = ['888888']

br.form['SET-ATTRIBUTE helm ocnRole2 2 Y'] = ['CEO']

br.form['SET-ATTRIBUTE helm ocnState 2 Y'] = ['Alaska']

br.form['SET-ATTRIBUTE helm ocnCountry 2 Y'] = ['US']

br.submit()

print br
