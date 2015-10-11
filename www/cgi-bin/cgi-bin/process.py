#!/usr/bin/python

import cgi
import cgitb
import os
import thread
import commands
cgitb.enable()

print "Content-type: text/html\n"

data=cgi.FieldStorage()
ip=commands.getoutput('cat jobtracker.txt')
print ip	
inpt=data['input'].value
inpt_file=data['input_file'].value
output=data['output'].value
mapr=data['mapper'].value
redu=data['reducer'].value
word=data['word'].value

print inpt+"</br>"
print inpt_file+"</br>"
print output+"</br>"
print mapr+"</br>"
print redu+"</br>"
print word+"</br>"

if inpt!='none':
	inpt_l=inpt.split('/')
	inpt_len=len(inpt_l)
	print inpt_l
	print inpt_len
	cmd_to_put='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip+''' "hadoop fs -put '''+inpt+''' /user_input/"'''
	os.system(cmd_to_put)
if redu=='wordcount':
	cmd_to_pro='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip+''' "hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /user_input/'''+inpt_l[inpt_len-1]+''' '''+output+'''"'''
	os.system(cmd_to_pro)
