#!/usr/bin/python2

import os 
import sys
import commands as cmd
import cgi
import cgitb
cgitb.enable()


print 'Content-type: text/html'
print '\n'


form = cgi.FieldStorage()

"""---------checking for form values --------------"""

if form['blk_size'].value() == '':
  blk_size = 'n'
elif 
  blk_size = form['blk_size'].value()

if form['replication'].value() == '':
  replication = 'n'
elif 
  replication = form['replication'].value()

if form['heartBeat'].value() == '':
  heartBeat = 'n'
elif 
  heartBeat= form['heartBeat'].value()

if form['scheduler'].value() == '':
  scheduler='n'
elif
  scheduler = form['scheduler'].value()

if form['chk_point'].value() == '':
  chk_point = 'n'
elif
  chk_point = form['chk_point'].value()

if form['minHeap'].value() == '':
  minHeap = 'n'
elif
  minHeap = form['minHeap'].value()

if form['maxHeap'].value() == '':
  maxHeap == 'n'
elif
  maxHeap = form['maxHeap'].value() 


"""-------------------------end of check------------------"""



"setting up namenode"
_file = open("namenode.txt","r")

namenode_ip = str(_file.readline().strip('\n'))

_file.close()
s = "./namenode.py "+namenode_ip+" y "+replication+" "+blk_size
if os.popen("ssh -n "+namenode_ip+ " nohup "+s+" > /dev/null 2>&1 &"):   ######test it for the errors
  sys.exit(1)

		''' 
			now we need to ssh and start the command and check for the exit code to confirm namenode setup			
                '''

"setting up jobtracker"

_file = open("jobtracker.txt","r")

jobtracker_ip = str(_file.readline().strip('\n'))

_file.close()
s = "./jobtracker.py "+namenode_ip+" "+jobtracker_ip+" "+scheduler

if os.popen("ssh -n "+jobtracker_ip+ " nohup "+s+" > /dev/null 2>&1 &"):   ######test it for the errors
  sys.exit(1)

"setting up datanodes"
_file = open("datanodes.txt","r")

arr = _file.read()

_file.close()

m = ( len(arr)/5 )* 5
n = len(arr) % 5


for i in range(0,m,5):
  a = "ssh -n "+str(arr[i].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  b = "ssh -n "+str(arr[i+1].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  c = "ssh -n "+str(arr[i+2].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  d = "ssh -n "+str(arr[i+3].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  e = "ssh -n "+str(arr[i+4].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  tempFn = lambda x: os.popen(x) 
  thread.start_new_thread( tempFn(a), () )
  thread.start_new_thread( tempFn(b), () )
  thread.start_new_thread( tempFn(c), () )
  thread.start_new_thread( tempFn(d), () )
  thread.start_new_thread( tempFn(e), () )

for i in range (m,m+n):
  s = "ssh -n "+str(arr[i].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+heartBeat+" > /dev/null 2>&1 &"
  os.popen(s)
  

"setting up tasktrackers"
_file = open("tasktracker.txt","r")

arr = _file.read()

_file.close()

m = ( len(arr)/5 )* 5
n = len(arr) % 5


for i in range(0,m,5):
  a = "ssh -n "+str(arr[i].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  b = "ssh -n "+str(arr[i+1].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  c = "ssh -n "+str(arr[i+2].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  d = "ssh -n "+str(arr[i+3].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  e = "ssh -n "+str(arr[i+4].strip('\n'))+" nohup ./datanode.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  tempFn = lambda x: os.popen(x) 
  thread.start_new_thread( tempFn(a), () )
  thread.start_new_thread( tempFn(b), () )
  thread.start_new_thread( tempFn(c), () )
  thread.start_new_thread( tempFn(d), () )
  thread.start_new_thread( tempFn(e), () )

for i in range (m,m+n):
  s = "ssh -n "+str(arr[i].strip('\n'))+" nohup ./tasktracker.py "+namenode_ip+" "+jobtracker_ip+" > /dev/null 2>&1 &"
  os.popen(s)

