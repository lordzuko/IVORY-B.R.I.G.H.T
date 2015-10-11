#!/usr/bin/python

import cgi
import os
import commands
import cgitb
import thread
#cgitb.enable()

print "Content-type: text/html\n"

form=cgi.FieldStorage()

hb=form['hb'].value
rep=form['rep'].value
siz=str(int(form['siz'].value)*1024*1024*2)
port=form['port'].value

class g:
	def __init__(self):
		self.j=0
	def inc(self):
		self.j+=1
a=g()

os.system("sudo sed -i '/<configuration>/a <property><name>dfs.name.dir</name><value>/name</value></property><property><name>dfs.heartbeat.interval</name><value>"+hb+"</value></property><property><name>dfs.replication</name><value>"+rep+"</value></property><property><name>dfs.block.size</name><value>"+siz+"</value></property><property><name>dfs.http.address</name><value>0.0.0.0:"+port+"</value></property>' hadoop/nn_hdfs-site.xml")

def conf_hdfs_file(ip):
	print "node_"+ip
		
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh stop namenode" &> /dev/null')
	print "nn_t_"+ip+"</br>"
	os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/nn_hdfs-site.xml "+ip+":/etc/hadoop/hdfs-site.xml")
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh start namenode" &> /dev/null')
	a.inc()

ip_namenode=commands.getoutput('cat namenodes.txt')
print ip_namenode
thread.start_new_thread(conf_hdfs_file,(ip_namenode,))

while True:	
	if a.j<1:
		#print str(a.j)+'_break</br>'
		pass	
	else:	
		#print str(a.j)+'_pass</br>'
		os.system('rm -rf hadoop;cp -rf backup hadoop')
		break

