#!/usr/bin/python

import cgi
import os
import commands
import cgitb
import thread
#cgitb.enable()

print "Content-type: text/html\n"

form=cgi.FieldStorage()

if form.has_key('on'):
	ip_namenode=commands.getoutput('cat namenodes.txt')
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -safemode enter" &>/dev/null')
	print "SafeMode: on"
elif form.has_key('off'):
	ip_namenode=commands.getoutput('cat namenodes.txt')
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -safemode leave" &>/dev/null')
	print "SafeMode: off"
else:
	ip_namenode=commands.getoutput('cat namenodes.txt')
	x=commands.getoutput('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -safemode get" 2> /dev/null')
	print x
