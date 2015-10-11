#!/usr/bin/python

import os 
import sys

dir_name=raw_input("Enter path: \n>")
f_nis = open("/etc/exports","a")
s = dir_name+"   192.168.0.0/24(rw)"
f_nis.write(s)
f_nis.close()
os.popen("service nfs restart; exportfs -r ; setenforce 0; iptables -F")
0  
