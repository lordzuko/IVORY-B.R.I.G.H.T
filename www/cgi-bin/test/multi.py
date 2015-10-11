#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html'
print '\n'


print "<form action=\'get2.py\'>"

for i in range(5):
  print "<select multiple name=\'x"+str(i)+"\'/>"
  print "<option>Namenode</option>"
  print "<option>Datanode</option>"
  print "<option>JobTracker</option><br/>"

print "<input type=\'submit\' />"
print "</form>"
