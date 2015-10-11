#!/usr/bin/python2

import os
import sys
import commands as cmd
import cgi
import cgitb
cgitb.enable()

print 'Content-type: text/html'
print '\n'

form = cgi.FormContent()
print "<h1>"+str(type(form))+"</h1>"
beer=[]
l = int(cmd.getoutput("cat nodeInfo.txt | wc -l").strip('\n'))
for i in range (l):
  a = "multi"+str(i)
  print "<h1>"+str(type(form[a]))+"</h1>"
  beer.append(form[a])


for i in range(l):
  for j in beer[i]:
  	print "<h1>"+j+"</h1>"
