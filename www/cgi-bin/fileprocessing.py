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

_file=form[l[0]].value
_type=form[l[1]].value


if _type=="file":
  status,output=cmd.getstatusoutput("sudo hadoop fs -rm "+_file)
else:
  status,output=cmd.getstatusoutput("sudo hadoop fs -rmr "+_file)

print 'Content-type: text/html'
print 'location: http://192.168.5.53/FileManager.html'
print '\n'
