#!/usr/bin/python

import os
import cgi
import cgitb
import thread
cgitb.enable()

print "Content-type: text/html\n"
task_trk=[]
try:
	print "<pre> select tasktracker</br>"
	print "<form action='config_tracker.py' method='POST'>"
	with open('datanodes.txt') as tt:
		for each_ip in tt:
			task_trk.append(each_ip)
			print "<input name='tt' type='checkbox' value="+each_ip+" \>"+each_ip+"</br>"
	print "select jobtracker</br>"
	with open('elig.txt') as jt:
		for each_ip in jt:
			if each_ip not in task_trk:
				print "<input name='jt' type='checkbox' value="+each_ip+" \>"+each_ip+"</br>"
	print "<input type='submit' value='create' \></form></pre>"
except:
	print "no host"
