#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
print "Content-type: text/html\n"

print "Enter ur req......"

x='''<form action="nis_conf.py" method="POST">
	ip for nis:	<input type="text" name="nis" \></br>
	ip for nfs:	<input type="text" name="nfs" \></br>
	file containing user name and password sepreted by ':' :	<input type="file" name="up" \></br>

	<input type="submit" ></form>'''

print x
