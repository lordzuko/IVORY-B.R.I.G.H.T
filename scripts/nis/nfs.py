#!/usr/bin/python2


import os
import sys
import commands as cmd

def main(argv):
  if len(argv) != 1:
    sys.exit("Usage ./nfs.py <nfs_ip>")
  
  nfs = argv[0]
  
  #install nfs-utils
  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nfs+' "yum install nfs-utils --quiet -y" &> /dev/null')
  
  #make entry in /etc/exports file
  exp='''sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'''+nfs+''' "echo '/user   *(rw,sync)' | cat >> /etc/exports"'''

  os.popen(exp)
  #restart nfs service
  os.system('sshpass -p "redhat" ssh -o StrictHostKeyChecking=no root@'+nfs+' "service nfs restart;exportfs -r;setenforce 0;iptables -F;"')


if __name__ == "__main__":
  main(argv[1:])
