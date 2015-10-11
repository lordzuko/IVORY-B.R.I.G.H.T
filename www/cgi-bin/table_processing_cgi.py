#!/usr/bin/python2

import cgi
import os
import sys
import commands as cmd
import cgitb
cgitb.enable()

print 'Content-type: text/html'
print '\n'

# values that will be coming from table

# <ip> <hostname> <hdd available> <slot available> <status>


form = cgi.FieldStorage()

a= form['ip'].value()
print '<h1>'+type(ip)+'</hi>'
b = form['hostname'].value()
c = form['hdd'].value()
d = form['slot'].value()
e = form['status'].value()


for i in range(len(ip)):
  print "<h1> ip = " +a[i]+"</h1>"
  print "<h1> hostname = " + b[i]+"</h1>"
  print "<h1> hdd = " + c[i]+"</h1>"
  print "<h1> slot = " + d[i]+"</h1>"
  print "<h1> status = " +e[i]+"</h1>"
  print "<p>----------------------------------------------</p>" 
 






