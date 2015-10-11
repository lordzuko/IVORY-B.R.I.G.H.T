#!/usr/bin/python

import os
import commands
import sys

print "content-type: text/html"
print "\n"

s=""
l=int(os.popen("sudo hadoop fs -ls / | wc -l").read().strip())
k="sudo hadoop fs -ls / | tail -%r |awk '{print $8}'"%(l-1)
name=os.popen(k).read().split('\n')
name=name[:-1]
k="sudo hadoop fs -ls / | tail -%r |awk '{print $1}'|awk -F'r' '{print $1}'"%(l-1)
ftype=os.popen(k).read().split('\n')
ftype=ftype[:-1]
rep="sudo hadoop fs -ls / | tail -%r |awk '{print $2}'"%(l-1)
rep=os.popen(rep).read().split('\n')
rep=rep[:-1]
size="sudo hadoop fs -ls / | tail -%r |awk '{print $5}'"%(l-1)
size=os.popen(size).read().split('\n')
size=size[:-1]
l=l-1

f=open("filelist.txt","w")
for i in range(0,l):
	if (ftype[i]=='d'):
		s=""+name[i]+":directory:"+rep[i]+":"+size[i]+"\n"
		print s
	else:
		s=""+name[i]+":file:"+rep[i]+":"+size[i]+"\n"
		print s
	f.write(s)
f.close()



	
