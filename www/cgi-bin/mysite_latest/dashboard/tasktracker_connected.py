#!/usr/bin/python2

import os

print 'Content-type: text/html'
print '\n'
_file = open("task_conn.txt","r")
s=_file.readline().strip();
_file.close();
 
print s+"<i class=\"icon-arrow-up\"></i>"
