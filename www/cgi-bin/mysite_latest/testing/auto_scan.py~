#!/usr/bin/python2

import os
import sys
import commands as cmd
import cgitb
import cgi
cgitb.enable()
import thread
#print 'Content-type: text/html\n'

#orm=cgi.FieldStorage()
#host_ip = form['host_ip'].value


os.popen("scan_cluster.py")
#after this a file nodes will be generated
#it will have the ip of all the nodes in our cluster
#now we want to select suitable nodes for namenode , jobtracker, tasktracker and datanode
host_ip = '127.0.0.1'
with open('nodes') as f:
  for each in f:
    client_ip=str(each.strip('\n'))
    s = 'sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+' "nohup available_hdd.py %s" > /dev/null 2>&1 &' %(host_ip)
    os.popen(s)		
    


s = "cat /root/Desktop/testing/temp/* > /root/Desktop/testing/selection_list"
#os.chdir("/root/Desktop/testing/temp/")
os.popen(s)
os.popen("best_selector.py")
