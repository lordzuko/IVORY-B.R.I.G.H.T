#!usr/bin/python
import os
import cgitb
cgitb.enable()

print "Content-type: text/html\n"

data=cgi.FieldStorage()

#network=data['net'].value
network='192.168.0.254/24'
list_sys=[]
def scanip(network):
	os.system('sudo nmap -sP '+network+' | grep report   > ip_add.txt')
	dic_sys={}
	with open('ip_add.txt') as f:
		for each in f:
			x=each.split()[5]
			l=len(x)-1
			ip=x[1:l]

			dic_sys['ip']=ip
			os.system('mkdir data/'+ip)
			os.system(" sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+"'mkdir  /project'")
#-------------hdd---------------------#
			os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'parted -l /dev/sda > /project/hdd.txt'")
			os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no "+ip+":/project/hdd.txt  data/"+ip)
			dic={}
			with open('data/'+ip+'/hd.txt') as f:
				i=0
				for each in f:
					dic[i]=each
					i+=1
				mx=int(dic[1].split()[2][0:3])
				mn=int(dic[i-3].split()[2][0:3])
				rem=mx-mn
			dic_sys['hd']=rem
#-------------------RAM----------------#
	
			os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'free -m | grep Mem > /project/ram.txt'")
			os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no   "+ip+":/project/ram.txt         data/"+ip)
			with open('data/'+ip+'/ram.txt') as f:
				for each in f:
					ram=each.split()[1]
				dic_sys['ram']=ram

#-------------------cpu-------------------#
	
			os.system("sudo sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+ip+" 'cat /proc/cpuinfo | grep processor | wc -l > project/cpu.txt'")
			os.system("sudo sshpass -p 'redhat' scp -o StrictHostKeyChecking=no "+ip+":/project/cpu.txt  data/"+ip)
			with open('data/'+ip+'/cpu.txt') as f:
				cpu=f.readline()
			dic_sys['cpu']=cpu
	

scanip(network)		

