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

nis=form['nis'].value()
nfs=form['nfs'].value()

#this func calls the command ./nis_client.py --> it's used this way for multithreading

os.popen("echo -e "+nis+" "+nfs+"| cat > nis_nfs.txt")

def nis_client(client_ip,nis,nfs):
  os.popen("./nis_client.py"+client_ip+" "+" "+nis+" "+nfs)


def ypbind_installation(client_ip):
  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+" 'setenforce 0;iptables -F'")
  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+' "yum install ypbind --quiet -y" &> /dev/null')

def nis_server(n)
  os.popen("./nis_server.py "+n)

def nfs_server(n)
  os.popen("./nfs.py "+n)

nis_server(nis)
nfs_server(nfs)


#we have to setup nis_clients which are 
with open('nodes.txt') as f:
	for each in f:
		client_ip=str(each.strip('\n'))
		thread.start_new_thread(ypbind_installation,(client_ip,))		
		thread.start_new_thread(nis_client,(client_ip,nis,nfs))
