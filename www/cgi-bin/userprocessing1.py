#!/usr/bin/python2

import os
import sys
import commands as cmd
import time
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

l = form.keys()

_uname=form[l[0]].value
_dir=form[l[1]].value

os.popen("sudo hadoop fs -rmr "+_dir)

##write code to block or remove a user

print 'Content-type: text/html'
print 'location: http://192.168.5.53/UserConsole.html'
print '\n'
