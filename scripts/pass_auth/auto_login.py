#/usr/bin/python2

import cgi
import os
import sys

print "content-type:text/html"
print

login = cgi.FormContent()

""" code for create user """
username = login.username
password = login.password


if os.system("./store_user_pass.py "+ username) == 0:
  login succesful
else 
  unsuccessful login message
  
""" login authentication """
  
username = login.username
password = login.password



""" password recovery mode """

username = login.username
password = login.password

os.popen("./store_user_pass.py "+ username)

print "ur password has been recovered"
