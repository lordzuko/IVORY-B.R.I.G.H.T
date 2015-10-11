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

blk_size = 'n'
replication = 'n'
heartBeat = 'n'
chk_point = 'n'
scheduler = "FAIR"
minHeap = 'n'
maxHeap = 'n'

"setting up namenode"
_file = open("namenode.txt","r")

namenode_ip = str(_file.readline().strip('\n'))

_file.close()

#s = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+namenode_ip+' "nohup ./namenode.py %s y %s %s" > /dev/null 2>&1 &') %(namenode_ip,replication,blk_size)
s = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+"127.0.0.1"+' "nohup firefox" > /dev/null 2>&1 &') #%(namenode_ip,replication,blk_size)
if os.popen(s) > 0:   ######test it for the errors
  sys.exit("<h1>exit here</h1>")

''' 
now we need to ssh and start the command and check for the exit code to confirm namenode setup			
'''

"setting up jobtracker"

_file = open("jobtracker.txt","r")

jobtracker_ip = str(_file.readline().strip('\n'))

_file.close()

s = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+jobtracker_ip+' "nohup ./jobtracker.py %s %s %s" > /dev/null 2>&1 &') % (namenode_ip,jobtracker_ip,scheduler)
if os.popen(s) > 0:   ######test it for the errors
  sys.exit(1)

"setting up datanodes"
_file = open("datanodes.txt","r")

arr = _file.read()

_file.close()

m = ( len(arr)/5 )* 5
n = len(arr) % 5


for i in range(0,m,5):
  a = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)
  b = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+1].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)
  c = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+2].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)
  d = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+3].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)
  e = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+4].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)

  tempFn = lambda x: os.popen(x) 
  thread.start_new_thread( tempFn(a), () )
  thread.start_new_thread( tempFn(b), () )
  thread.start_new_thread( tempFn(c), () )
  thread.start_new_thread( tempFn(d), () )
  thread.start_new_thread( tempFn(e), () )

for i in range (m,m+n):
  s = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i].strip('\n'))+' "nohup ./datanode.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,heartBeat)
  os.popen(s)
  

"setting up tasktrackers"
_file = open("tasktracker.txt","r")

arr = _file.read()

_file.close()

m = ( len(arr)/5 )* 5
n = len(arr) % 5


for i in range(0,m,5):
  a = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  b = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+1].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  c = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+2].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  d = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+3].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  e = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i+4].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  tempFn = lambda x: os.popen(x) 
  thread.start_new_thread( tempFn(a), () )
  thread.start_new_thread( tempFn(b), () )
  thread.start_new_thread( tempFn(c), () )
  thread.start_new_thread( tempFn(d), () )
  thread.start_new_thread( tempFn(e), () )

for i in range (m,m+n):
  s = ('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+str(arr[i].strip('\n'))+' "nohup ./tasktracker.py %s %s " > /dev/null 2>&1 &' ) %(namenode_ip,jobtracker_ip)
  os.popen(s)

