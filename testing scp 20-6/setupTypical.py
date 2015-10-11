#!/usr/bin/python2

import thread
import os 
import sys
import commands as cmd
import cgi
import cgitb
cgitb.enable()
import time

print 'Content-type: text/html'
print '\n'

form = cgi.FieldStorage()

blk_size = 'n'
replication = 'n'
heartBeat = 'n'
chk_point = 'n'
scheduler = "FAIR"
minHeap = 'n'
maxHeap = 'n'

print "<h1>0%</h1>"
#os.system("auto_scan.py")
print "<h1>10%</h1>"
"setting up namenode"
_file = open("namenode","r")

namenode_ip = str(_file.readline().strip('\n'))

_file.close()
os.system('sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no /root/Desktop/testing/namenodef/*.* '+namenode_ip+':/etc/hadoop/')
time.sleep(1)
s = ('sudo sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+namenode_ip+' "nohup hadoop namenode -format" > /dev/null 2>&1 &') 
if os.system(s) > 0:   ######test it for the errors
  sys.exit("<h1>exit here</h1>")

time.sleep(5)

s = ('sudo sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+namenode_ip+' "nohup hadoop-daemon.sh start namenode" > /dev/null 2>&1 &') 
if os.system(s) > 0:   ######test it for the errors
  sys.exit("<h1>exit here</h1>")

print "<h1>20%</h1>"
''' 
now we need to ssh and start the command and check for the exit code to confirm namenode setup			
'''

"setting up jobtracker"

_file = open("jobtracker","r")

jobtracker_ip = str(_file.readline().strip('\n'))

_file.close()
os.system('sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no /root/Desktop/testing/jobtrackerf/*.* '+jobtracker_ip+':/etc/hadoop/')
time.sleep(1)
s = ('sudo sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+jobtracker_ip+' "nohup hadoop-daemon.sh start jobtracker" > /dev/null 2>&1 &')
time.sleep(5)
if os.system(s) > 0:   ######test it for the errors
  sys.exit(1)

print "<h1>40%</h1>"
"setting up datanode"
_file = open("datanode","r")

arr = []
for i in _file:
  arr.append(i)

_file.close()
time.sleep(6)

for i in arr:
  os.system('sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no /root/Desktop/testing/datanodef/*.* '+i.strip('\n')+':/etc/hadoop/')
  time.sleep(1)
  a = ('sudo sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i.strip('\n')+' "nohup hadoop-daemon.sh start datanode " > /dev/null 2>&1 &' ) 
  
  tempFn = lambda x: os.system(x) 
  thread.start_new_thread( tempFn, (a,) )

time.sleep(6)
print "<h1>75%</h1>"
"setting up tasktracker"
_file = open("tasktracker","r")

brr = []

for i in _file:
  brr.append(i)

_file.close()



for i in brr:
  os.system('sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no /root/Desktop/testing/tasktrackerf/*.* '+i.strip('\n')+':/etc/hadoop/')
  time.sleep(1)
  a = ('sudo sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+i.strip('\n')+' "nohup hadoop-daemon.sh start tasktracker " > /dev/null 2>&1 &' )   
  tempFn = lambda   x: os.system(x) 
  thread.start_new_thread( tempFn, (a,) )

print "<h1>100%</h1>"
print "Wait for few moments..."
