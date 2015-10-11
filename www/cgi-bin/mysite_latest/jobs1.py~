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

username = form['username'].value
path = "/home/"+username+"/"+form['path'].value
example= form['example'].value
output = form['output'].value

s = "hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar %s %s %s" %(example,path,output)
"""
print "<h1>"+str(username)+"</h1>"
print "<h1>"+str(path)+"</h1>"
print "<h1>"+str(example)+"</h1>"
print "<h1>"+str(output)+"</h1>"
"""
os.popen(s)



print 'location: http://127.0.0.1/mysite_latest/Jobs.html'
print '\n'
