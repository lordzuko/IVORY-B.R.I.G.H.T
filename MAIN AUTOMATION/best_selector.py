#!/usr/bin/python2

import os
import sys
import commands as cmd


os.popen("sort  -k3 -k2 -n -r  selection_list | head -1| awk -F' ' '{print $1}' > /root/Desktop/testing/namenode").read()
os.popen("sort   -k3 -k2 -n -r  selection_list | head -2|tail -1| awk -F' ' '{print $1}' > /root/Desktop/testing/jobtracker").read()
linecount=os.popen("sort -k3 -k2 -n -r  selection_list | wc -l").read()
linecount.strip()
linecount=int(linecount) - 2 
os.popen("sort -k3 -k2 -n -r  selection_list | tail -"+str(linecount)+"| awk -F' ' '{print $1}' > /root/Desktop/testing/datanode").read()
os.popen("sort -k3 -k2 -n -r  selection_list | tail -"+str(linecount)+"| awk -F' ' '{print $1}' > /root/Desktop/testing/tasktracker").read()
