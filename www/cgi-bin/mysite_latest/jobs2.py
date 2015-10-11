#!/usr/bin/python2

import cgi
import os
import sys
import commands as cmd 
import cgitb
cgitb.enable()

print 'Content-type: text/html'
#print '\n'

try: #windows need stdio set for binary mode
	import msvcrt
	msvcrt.setmode(0,os.O_BINARY)#stdin=0
	msvcrt.setmode(1,os.O_BINARY)#stdout=1
except ImportError:
	pass
form=cgi.FieldStorage()
#Anested Field storage instance hols the file
fileitem= form['file']
fileitem2= form['file2']

#Test if the file was uploaded
if fileitem.filename:
	#strip leading path from file name to avoid directory traversal attacks
	fn= os.path.basename(fileitem.filename)
	open('files/'+fn,'wb').write(fileitem.file.read())
	message='The file was uploaded successfully'
else: 
   	message='No file was uploaded'
if fileitem2.filename:
	#strip leading path from file name to avoid directory traversal attacks
	fn2= os.path.basename(fileitem2.filename)
	open('files/'+fn2,'wb').write(fileitem2.file.read())
	message2='The file2 was uploaded successfully'
else: 
   	message2='No file2 was uploaded'

username = form['username'].value
path = form['path'].value
mapper= "/var/www/cgi-bin/files/"+fn+""
reducer= "/var/www/cgi-bin/files/"+fn2+""
output = form['output'].value

s = "sudo hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -mapper 'python %s' -reducer 'python %s' -input %s -output %s" %(mapper,reducer,path,output)
"""
print "<h1>"+s+"</h1>"

print "<h1>"+str(username)+"</h1>"
print "<h1>"+str(path)+"</h1>"
print "<h1>"+str(mapper)+"</h1>"
print "<h1>"+str(reducer)+"</h1>"
print "<h1>"+str(output)+"</h1>"
"""
os.popen(s)



print 'location: http://127.0.0.1/mysite_latest/Jobs.html'
print '\n'
