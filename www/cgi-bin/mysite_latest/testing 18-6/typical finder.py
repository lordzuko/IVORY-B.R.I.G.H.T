#!/usr/bin/python2
import os
import sys
import commands



namenode_ip=os.popen("sort -t \" \" -k3 -k2 -n -r  ipsort| head -1| awk -F' ' '{print $1}' > namenode.txt").read()
jobtracker_ip=os.popen("sort -t \" \" -k3 -k2 -n -r  ipsort| head -2|tail -1| awk -F' ' '{print $1}' > jobtracker.txt").read()
linecount=os.popen("sort -t \" \" -k3 -k2 -n -r  ipsort| wc -l").read()
linecount.strip()
linecount=int(linecount) - 2
datanodes=os.popen("sort -t \" \" -k3 -k2 -n -r  ipsort| tail -"+str(linecount)+"| awk -F' ' '{print $1}'> datanodes.txt").read()
print datanodes 

