#!/usr/bin/python

import cgi
import os
import commands
import cgitb
import thread
#cgitb.enable()

print "Content-type: text/html\n"

form=cgi.FieldStorage()

print "Change Heartbeat|Replications|BlockSize|Port</br>"
x="""<form action='default_change.py' method='POST'>
	Enter heartBeat: <input type='text' name='hb' value='10'></br>
	Enter number of replication: <input type='text' name='rep' value='3'></br>
	Enter BlockSize in MB: <input type='text' name='siz' value='64'></br>
	Enter managment port for namenode: <input type='text' name='port' value='50070'></br>
	<input type='submit' name='submit' value='change'></form></br></br></br><hr></br></br>
	<form action='mode_change.py' method='POST'>
	SafeMode:<input type='submit' name='on' value='ON'><input type='submit' name='off' value='OFF'><input type='submit' name='state' value='status'>
	</form>
	</br></br></br><hr></br></br>
	<form action='start_change.py' method='POST'>
	Datanode: <input type='submit' name='start' value='start-all'><input type='submit' name='stop' value='stop-all'>
	</form></br></br></br><hr></br></br>
"""
print x

try:
	print "<pre> allow datanodes                   deny datanode</br>"
	print "<form action='config_datanode.py' method='POST'>"
	with open('datanodes.txt') as hv:
		for each_ip in hv:
			lent=len(each_ip)
			print "<input name='allow' type='checkbox' value="+each_ip+" \>"+each_ip[:lent-1]+"                         <input name='deny' type='checkbox' value="+each_ip+" \>"+each_ip[:lent-1]+"</br>"

	print "<input type='submit' value='refresh' \></form></pre>"
except:
	print "no Datanode"

