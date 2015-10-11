#!/usr/bin/python2

import sys
import cgi
import os

print 'Content-type:text/html \n\n'


form = cgi.FieldStorage()

username = form['username'].value
password = form['password'].value


_file = open("Installation.html")

if os.system("./store_user_pass "+username) == 0:
  if os.system("./user_pass "+username) ==0:
    print _file.read()
    

