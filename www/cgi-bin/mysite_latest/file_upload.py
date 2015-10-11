#!/usr/bin/python2
import cgi,os
import cgitb;cgitb.enable()

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

print "Content-type: text/html"
print 

print "<p>%s %s</p>"%(message,message2)
