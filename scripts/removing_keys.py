#!/usr/bin/python2
import os 
import sys
os.popen("nmap -sP -n 192.168.0.0/24 | grep 192. | awk -F' ' '{print $5}' > node2.txt")
node_file  = open("node2.txt")
l=int(os.popen("cat node2.txt | wc -l").read())-2
for nodes in range(0,l):
  '''if ((nodes == "'192.168.0.254'")  (nodes == "192.168.0.250")):
    print ( " "+nodes+" "+str(type(nodes)))
    continue
'''
  node=node_file.readline().strip()
  print (node+"is shutting down")
  s = "ssh root@%s reboot -f" % (node)
  os.popen(s)

  
