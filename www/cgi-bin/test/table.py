#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html'
print '\n'


print "<form action=\'get.py\'>"

for i in range(5):
  print "<input name=\'x"+str(i)+"\'/>"

print "<input type=\'submit\' />"
print "</form>"
