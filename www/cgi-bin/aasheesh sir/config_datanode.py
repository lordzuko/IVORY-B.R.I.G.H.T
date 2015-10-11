#!/usr/bin/python

import cgi
import os
import commands
import cgitb
import thread
#cgitb.enable()

print "Content-type: text/html\n"

form=cgi.FieldStorage()
#---------------------ALLOW----------------------$$$$
nn=str(form['allow']).split('MiniFieldStorage')
#print nn
nn_l=len(nn)-1
nn_ips=nn[1:]
#print nn_ips
#print '</br>'+str(nn_l)

for i in range(nn_l):
	nn_i=nn_ips[i][11:]
	if nn_l==1:
		nn_i_l=len(nn_i)-2
		nn_ip=nn_i[:nn_i_l]
	else:
		nn_i_l=len(nn_i)-4
		if int(i) < int(nn_l-1):
			nn_ip=nn_i[:nn_i_l]
		else:
			nn_ip=nn_i[:nn_i_l+1]	
		#print nn_ip+"</br>"
	with open('hostallow.txt','a') as nf:
		nf.write(nn_ip+'\n')

##-------------------------DENY-------------------$$$$

dn=str(form['deny']).split('MiniFieldStorage')
#print dn
dn_l=len(dn)-1
dn_ips=dn[1:]
#print dn_ips
#print '</br>'+str(dn_l)

for i in range(dn_l):
	dn_i=dn_ips[i][10:]
	if dn_l==1:
		dn_i_l=len(dn_i)-2
		dn_ip=dn_i[:dn_i_l]
	else:
		dn_i_l=len(dn_i)-4
		if int(i) < int(dn_l-1):
			dn_ip=dn_i[:dn_i_l]
		else:
			dn_ip=dn_i[:dn_i_l+1]	
		#print dn_ip+"</br>"
	with open('hostdeny.txt','a') as df:
		df.write(dn_ip+'\n')

ip_namenode=commands.getoutput('cat namenodes.txt')
allow='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip_namenode+''' "sed -i '/<configuration>/a <property><name>dfs.hosts</name><value>/etc/hadoop/hostallow.txt</value></property>' /etc/hadoop/hdfs-site.xml"'''

deny='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip_namenode+''' "sed -i '/<configuration>/a <property><name>dfs.hosts.exclude</name><value>/etc/hadoop/hostdeny.txt</value></property>' /etc/hadoop/hdfs-site.xml"'''

os.system(allow)
os.system(deny)
os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -refreshNodes"')
