#!/usr/bin/python

import os
import cgi
import cgitb
import thread
cgitb.enable()

rec=cgi.FieldStorage()

print "Content-type: text/html\n"


class g:
	def __init__(self):
		self.j=0
	def inc(self):
		self.j+=1

a=g()

#---------------------config tasktracker----------------------#
def config_tt(ip):
	check='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip
	check_status=os.system(check)
	if check_status==0:
		os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/mapred-site.xml "+ip+":/etc/hadoop/")
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh start tasktracker" &> /dev/null')	
	a.inc()
#-----------------------config jobtracker----------------------#
def config_jt(ip):
	check='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip
	check_status=os.system(check)
	if check_status==0:
		os.system("sudo sed -i '/<configuration>/a <property><name>mapred.job.tracker</name><value>"+ip+":9002</value></property>' hadoop/mapred-site.xml")
		os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/mapred-site.xml "+ip+":/etc/hadoop/")
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh start jobtracker" &> /dev/null')	
	a.inc()	


#--------------------------------job tracker-------------------------------#

jt=str(rec['jt']).split('MiniFieldStorage')
#print tt
jt_l=len(jt)-1
jt_ips=jt[1:]
#print tt_ips
#print '</br>'+str(tt_l)
for i in range(jt_l):
	jt_i=jt_ips[i][8:]
	if jt_l==1:
		jt_i_l=len(jt_i)-2
		jt_ip=jt_i[:jt_i_l]
	else:
		jt_i_l=len(jt_i)-4
		if int(i) < int(jt_l-1):
			jt_ip=jt_i[:jt_i_l]
		else:
			jt_ip=jt_i[:jt_i_l+1]	
	print jt_ip+"</br>"
	with open('jobtracker.txt','a') as jf:
		jf.write(jt_ip+'\n')
	thread.start_new_thread(config_jt,(jt_ip,))


#--------------------------------task tracker------------------------------#
tt=str(rec['tt']).split('MiniFieldStorage')
#print tt
tt_l=len(tt)-1
tt_ips=tt[1:]
#print tt_ips
#print '</br>'+str(tt_l)
for i in range(tt_l):
	tt_i=tt_ips[i][8:]
	if tt_l==1:
		tt_i_l=len(tt_i)-2
		tt_ip=tt_i[:tt_i_l]
	else:
		tt_i_l=len(tt_i)-4
		if int(i) < int(tt_l-1):
			tt_ip=tt_i[:tt_i_l]
		else:
			tt_ip=tt_i[:tt_i_l+1]	
	print tt_ip+"</br>"
	with open('tasktracker.txt','a') as tf:
		tf.write(tt_ip+'\n')
	#config_tt(tt_ip)os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/mapred-site.xml "+ip+":/etc/hadoop/")	
	thread.start_new_thread(config_tt,(tt_ip,))
while True:
	if a.j<(tt_l+jt_l):
		#print str(a.j)+'_break</br>'
		pass	
	else:	
		#print str(a.j)+'_pass</br>'
		os.system('rm -rf hadoop;cp -rf backup hadoop')
		break
