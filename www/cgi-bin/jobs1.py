#!/usr/bin/python2

import cgi
import os
import sys
import commands as cmd 
import cgitb
cgitb.enable()

print 'Content-type: text/html'
#print '\n'

form = cgi.FieldStorage()

#username = form['username'].value
path = form['path'].value
example= form['example'].value
output = form['output'].value

s = "sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar %s %s %s" %(example,path,output)
"""
print "<h1>"+str(username)+"</h1>"
print "<h1>"+str(path)+"</h1>"
print "<h1>"+str(example)+"</h1>"
print "<h1>"+str(output)+"</h1>"
"""
os.popen(s)



print 'location: http://192.168.5.53/Jobs.html'
print '\n'
