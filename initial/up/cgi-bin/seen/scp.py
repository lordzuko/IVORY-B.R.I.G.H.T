#!/usr/bin/python
import os
import sys

print "Content-type: text/html\n"

ip='192.168.122.2'
a="""'echo -e  "n\n\n+100M\nw\n"| fdisk  -cu /dev/sda ; partx -a /dev/sda'"""
d="""'echo -e  "d\n5\nw\n"| fdisk  -cu /dev/sda ; partx -a /dev/sda'"""
z=os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' '+a+' &> /dev/null' ) 
#sys.stdout=z
#print z
dic={}
with open('data/'+ip+'/hd.txt') as f:
	i=0
	for each in f:
		dic[i]=each
		i+=1
part_num=int(dic[i-3].split()[0])+1
print part_num
print 'sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mkfs.ext4 /dev/sda6"'
#y=os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mkdir /new111"')
y=os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mkfs.ext4 /dev/sda'+str(part_num)+'" &> /dev/null')
os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip+' "mount /dev/sda'+str(part_num)+' /f"')
print y
