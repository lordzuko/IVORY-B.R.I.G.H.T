#!/usr/bin/python2

import cgi

print "Content-Type: text/html \n\n"

reshtml = """
<html>
<head>
<title> Friends CGI Demo (dynamic screen) </title>
</head>

<body>
<h3> Friends list for : <i> %s </i> </h3>
Your name is : <b> %s </b> <br/>
You have <b> %s </b> friends.
</body>
</html>

"""

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who,who,howmany)
