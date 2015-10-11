#!/usr/bin/python2

import os 
import sys

#first scan all the nodes in the network

#os.popen("cat ssh.txt | ssh-keygen")
os.popen("export SSH_AUTH_SOCK=0")
os.popen("iptables -F")
os.popen("setenforce 0")
os.popen("sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/' /etc/ssh/ssh_config ")
os.popen("nmap -sP -n 192.168.0.0/24 | grep 192. | awk -F' ' '{print $5}' > nodes.txt")

node_file  = open("nodes.txt")

for nodes in node_file:
  s = "sshpass -p redhat ssh-copy-id root@%s" % (nodes)
  os.popen(s)


