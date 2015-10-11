#!/usr/bin/python2

print 'Content-type: text/html'
print '\n'


import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "<h1>"+str(len(form))+"</h1>"
for i in range(len(form)):
  print "<h1>"+str(form["x"+str(i)].value)+"</h1>"
