#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
print "Content-type: text/html\n"

print "Enter ur req......"

x='''<form action="scan.py" method="POST">
	RAM(in MB):	<input type="text" name="ram" \></br>
	HD(in GB):	<input type="text" name="hd" \></br>
	cpu(nos. of processor):	<input type="text" name="cpu" \></br>

	network:	<input type="text" name="net" \></br>
	<input type="submit" ></form>'''

print x
