#!/usr/bin/python2


import os
import sys
import commands as cmd

def main(argv):
  
  if len(argv) != 1:
    sys.exit("Usage ./nis_server.py <nis> ")
  
  nis = argv[0]
  
  

  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nis+' "yum install ypserv --quiet -y" &> /dev/null')

  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nis+' "ypdomainname hadoop"')

  #changes made in yp.conf file
  os.system("echo -e 'domain hadoop server "+nis+"' | cat >> nis/yp.conf")
  
  '''---------------------------------------/etc/yp.conf--------------------------------------------'''
  

  cmd_yp='''sudo sshpass -p "redhat" scp -o StrictHostKeyChecking=no nis/yp.conf '''+client_ip+''':/etc/'''
  os.popen(cmd_yp)	
  
  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nis+' "service ypserv stop;service ypserv start" &> /dev/null')

  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nis+' "make -C /var/yp" &> /dev/null')
  
if __name__ = "__main__":
  main(sys.argv[1:])
