#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import re
try: # Windows needs stdio set for binary mode.
	import msvcrt
	msvcrt.setmode (0, os.O_BINARY) # stdin= 0
	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
	pass
form = cgi.FieldStorage()
# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
	while True:
		chunk = f.read(chunk_size)
		if not chunk: break
		yield chunk
# A nested FieldStorage instance holds the file
fileitem = form['file']
# Test if the file was uploaded
if fileitem.filename:
# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	f = open('files/'+ fn+'', 'wb', 10000)
# Read the file in chunks
	for chunk in fbuffer(fileitem.file):
		f.write(chunk)
	f.close()
        hbsfn=re.sub(' ','_',fn)
	message = 'The file "' + fn + '" was uploaded successfully'
        os.system("sudo hadoop fs -put /var/www/cgi-bin/files/\'"+fn+"\' /"+hbsfn)
	os.system("sudo rm /var/www/cgi-bin/files/\'"+fn+"\'")
else:
	message = 'No file was uploaded'
print "Content-Type: text/html"

print "location:http://192.168.5.53/FileManager.html"
print
