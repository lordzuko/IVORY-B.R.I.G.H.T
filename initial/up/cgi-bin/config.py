#!/usr/bin/python

import os
import cgi
import cgitb
import thread
import commands
cgitb.enable()

rec=cgi.FieldStorage()
print "Content-type: text/html\n"
class g:
	def __init__(self):
		self.j=0
	def inc(self):
		self.j+=1

a=g()
os.system("sudo echo -e 'PATH=/usr/java/jdk1.7.0_51/bin:$PATH  export PATH'| cat >> hadoop/.bashrc")
os.system("sudo sed -i '/<configuration>/a <property><name>dfs.name.dir</name><value>/name</value></property>' hadoop/nn_hdfs-site.xml")
os.system("sudo sed -i '/<configuration>/a <property><name>dfs.data.dir</name><value>/data</value></property>' hadoop/dn_hdfs-site.xml")
def create_nn_file(ip):
	os.system("sudo sed -i '/<configuration>/a <property><name>fs.default.name</name><value>hdfs://"+ip+":9001</value></property>' hadoop/core-site.xml")
	a.inc()
#--------------Install packages------------------------#
def install(ip):
	a.inc()
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'setenforce 0;iptables -F'")
	os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'yum install jdk --quiet -y hadoop --quiet -y' &> /dev/null")


#-----------------------config core-site.xml-----------------#
def conf_nn_file(ip):
	os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/core-site.xml "+ip+":/etc/hadoop/")
	a.inc()

	
#--------------------config jps-------------------------#
def conf_jdk_file(ip):
	os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/.bashrc "+ip+":/root/.bashrc")
	a.inc()
	

#-------------config hdfs-site.xml-------------------------#
def conf_hdfs_file(node,ip):
	#print node
	if node=='nn':
		print "nn_t_"+ip+"</br>"
		os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/nn_hdfs-site.xml "+ip+":/etc/hadoop/hdfs-site.xml")
	else:
		print "dn_t_"+ip+"</br>"
		os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no hadoop/dn_hdfs-site.xml "+ip+":/etc/hadoop/hdfs-site.xml")
	a.inc()


#-------------------Partition-----------------------------#
def partition(node,ip):
	n="""'echo -e  "n\n\n+5G\nw\n"| fdisk  -cu /dev/sda ; partx -a /dev/sda'"""
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' '+n+' &> /dev/null')
	co='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip+''' "echo -e 'print\nq\n' | parted /dev/sda > /root/temp/hd.txt ; cat /root/temp/hd.txt | wc -l"'''
	x=commands.getoutput(co).split('\n')[2]
	print x
	part_num=int(x)-12
	###########SCP[/root/temp/hd.txt --> data/ip/]#################
	'''os.system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no root@"+ip+":/root/temp/hd.txt data/"+ip)
	dic={}
	with open('data/'+ip+'/hd.txt') as f:
		i=0
		for each in f:
			dic[i]=each
			i+=1
	part_num=int(dic[i-3].split()[0])'''
	os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mkfs.ext4 /dev/sda'+str(part_num)+'" &> /dev/null')
	#print node
	if node=='nn':
		#print node+"_if"
		os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'mkdir /name'")
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mount /dev/sda'+str(part_num)+' /name"')
		h_form='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+ip+''' "echo -e 'Y\n'| hadoop namenode -format"'''
		os.system(h_form)
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh start namenode" &> /dev/null')
	else:
		os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'mkdir /data'")
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mount /dev/sda'+str(part_num)+' /data"')
		os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "hadoop-daemon.sh start datanode" &> /dev/null')
	a.inc()
#----------------NN------------------------#
nn=str(rec['nn']).split('MiniFieldStorage')
#print nn
nn_l=len(nn)-1
nn_ips=nn[1:]
#print nn_ips
#print '</br>'+str(nn_l)

for i in range(nn_l):
	nn_i=nn_ips[i][8:]
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
	with open('namenodes.txt','a') as nf:
		nf.write(nn_ip+'\n')
	#conf_nn(nn_ip)		
	thread.start_new_thread(create_nn_file,(nn_ip,))
	thread.start_new_thread(install,(nn_ip,))
	thread.start_new_thread(conf_nn_file,(nn_ip,))
	thread.start_new_thread(conf_jdk_file,(nn_ip,))
	thread.start_new_thread(conf_hdfs_file,('nn',nn_ip))	
	thread.start_new_thread(partition,('nn',nn_ip))
print "</br>-----------------------------------</br>"

#--------------------dn--------------------#
dn=str(rec['dn']).split('MiniFieldStorage')
#print dn
dn_l=len(dn)-1
dn_ips=dn[1:]
#print dn_ips
#print '</br>'+str(dn_l)

for i in range(dn_l):
	dn_i=dn_ips[i][8:]
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
	with open('datanodes.txt','a') as df:
		df.write(dn_ip+'\n')
	#conf_nn(nn_ip)		
	thread.start_new_thread(install,(dn_ip,))
	thread.start_new_thread(conf_nn_file,(dn_ip,))
	thread.start_new_thread(conf_jdk_file,(dn_ip,))
	thread.start_new_thread(conf_hdfs_file,('dn',dn_ip))
	thread.start_new_thread(partition,('dn',dn_ip))


while True:	
	if a.j<(5*dn_l+6*nn_l):
		#print str(a.j)+'_break</br>'
		pass	
	else:	
		#print str(a.j)+'_pass</br>'
		os.system('rm -rf hadoop;cp -rf backup hadoop')
		break

