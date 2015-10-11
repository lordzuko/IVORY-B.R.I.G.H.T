#!/usr/bin/python

import os
import commands
import sys

print "content-type: text/html"
print "\n"

s=""
l=int(os.popen("sudo hadoop fs -ls /user | wc -l").read().strip())
k="sudo hadoop fs -ls /user | tail -%r |awk '{print $8}'"%(l-1)
directory=os.popen(k).read().split('\n')
directory=directory[:-1]
k="sudo hadoop fs -ls /user | tail -%r |awk '{print $8}'|awk -F'/' '{print $3}'"%(l-1)
name=os.popen(k).read().split('\n')
name=name[:-1]
l=l-1

f=open("userlist.txt","w")
for i in range(0,l):
	s=""+name[i]+":"+directory[i]+"\n"
	print s
	f.write(s)
f.close()

