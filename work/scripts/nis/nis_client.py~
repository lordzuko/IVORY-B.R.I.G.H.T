#!/usr/bin/python2


import os
import sys
import commands as cmd




def main(argv):
  
  if len(argv) != 3:
    sys.exit("Usage ./nis_client <client_ip>  <nis_server> <nfs_server>")
   
  #check if software is installed
  if(os.system("rpm -q ypbind") != 0):
    os.popen("yum install ypbind")
  else:
    print ("already install !!!")

  #entrying domain name in file /etc/sysconfig/network
  client_ip = argv[0]
  domainname = "hadoop"
  nis_server_ip = argv[1]
  nfs = argv[2]
  
 
 ## there is a function in nisClient_sw_installation.py for multithreading --> look fr it

  
  '''------------------------------------/etc/sysconfig/network-------------------------------------'''
  
  cmd_net='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+client_ip+''' "sed -i '/HOSTNAME/a NISDOMAIN=hadoop' /etc/sysconfig/network"'''
  os.popen(cmd_net)
  
  
  
  '''--------------------------------------/etc/nsswitch.conf---------------------------------------'''
  
  cmd_yp='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/nsswitch.conf '''+client_ip+''':/etc/'''
  os.popen(cmd_yp)

  
  '''------------------------------------/etc/pam.d/system-auth-------------------------------------'''
  cmd_pam='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/system-auth '''+client_ip+''':/etc/pam.d/'''
  os.popen(cmd_pam)
  

  '''---------------------------------- /etc/pam.d/system-auth-ac-----------------------------------'''
  cmd_pam_ac='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/system-auth-ac '''+client_ip+''':/etc/pam.d/'''
  os.popen(cmd_pam_ac)
  os.popen('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+' "service ypbind stop;service ypbind start" &> /dev/null')
  
  



  '''----------------------------autofs------------------------------'''
  ''' 
  	changes are made in two files for autofs :
        1)auto.misc
        2)auto.master
  '''
  os.popen('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+' "yum install autofs --quiet -y" &> /dev/null')
	
  #changes made in auto.misc file
  os.system("echo -e '*	"+nfs+":/user/&' | cat >> nis/auto.misc")
  misc='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/auto.misc '''+client_ip+''':/etc'''
  os.popen(misc)
  #changes has already been made to auto.master file
  master='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/auto.master '''+client_ip+''':/etc'''
  os.popen(master)

  os.popen('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+client_ip+' "service autofs stop; service autofs start" &> /dev/null')
  
  
  '''-----------------------------------------------------------------------------------------------------------------------------------'''
