#!/usr/bin/python2

import os
import sys
import commands as cmd
import cgi
import cgitb
cgitb.enable()

#it requires cluster to be set up
#it requires nis, nfs to be set up

nis = cmd.getoutput("cat nis_nfs.txt | awk -F' ' '{print $1}'").strip('\n')
nfs = cmd.getoutput("cat nis_nfs.txt | awk -F' ' '{print $2}'").strip('\n')

#users.txt is the file i'll be making in the background which will have information stored in this format
# user_name:password:file_quota:space_quota

with open('users.txt') as u:
  for each in u:
    m = each.strip('\n')
    n = m.split(":")
    user_name=str(n[0])
    password=str(n[1])
    file_quota=str(n[2])
    space_quota=str(n[3])
    
    x=os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+nis+" 'useradd "+user_name+"'")
	
    cmd_pas='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nis+''' "echo  -e '''+password+'''| passwd '''+user_name+''' --stdin" &> /dev/null'''
    #print cmd_pas		
    os.system(cmd_pas)
    #print str(x)+"</br>"
    os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nfs+' "mkdir -p /user/'+user_name+'; cp -rf /etc/skel/. /user/'+user_name+'"')
    os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nfs+' "mkdir -p /user/'+user_name+'; cp -rf /etc/skel/. /user/'+user_name+'"')
    os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop fs -mkdir /user/'+user_name+'; hadoop fs -chown  '+user_name+':'+user_name+' /user/'+user_name+'; hadoop fs -chmod 770 /user/'+user_name+'"')
    os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -setQuota '+file_quota+' /user/'+user_name+'"')
    os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+ip_namenode+' "hadoop dfsadmin -setSpaceQuota '+space_quota[:3]+' /user/'+user_name+'"')
