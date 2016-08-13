import cee

ocn = cee.cee()

ocn.loginusername = 'shrinivasan@collab.net'
ocn.password = 'l33ter'

ocn.login()


print ocn


ocn.username = 'contactzha'

ocn.email = 'contactzha@gmail.com'
ocn.realname = 'Shrinivasan T'
ocn.organization = 'zha'
ocn.firstname = 'Mr'
ocn.lastname = 'Shrini'
ocn.product = ['Cloud']
ocn.revenue = ['888888']
ocn.role = ['CEO']
ocn.state = ['Alaska']
ocn.country = ['US']


#ocn.create_user()
print ocn

ocn.new_organization = "CollabNet"
ocn.edit_user('shrini')
