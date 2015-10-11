#!/usr/bin/python

import cgi
import os
import commands
import cgitb
import thread
#cgitb.enable()

print "Content-type: text/html\n"

form=cgi.FieldStorage()

if form.has_key('start'):
	ip_namenode=commands.getoutput('cat namenodes.txt')
	key=commands.getoutput('cat key.txt')
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "chmod +x /usr/sbin/start-all.sh"')
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "chmod +x /usr/sbin/start-dfs.sh"')
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "chmod +x /usr/sbin/start-mapred.sh"')
	
