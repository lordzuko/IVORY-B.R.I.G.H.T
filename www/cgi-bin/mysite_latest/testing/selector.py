#!/usr/bin/python2

import os
import sys
import commands as cmd
import thread

def main(argv):
  
  if len(argv) != 2:
    sys.exit("Usage ./selector file_name host_ip")
  
  os.popen("scan_cluster")
  
  s = "/hadoop_setup/%s" %(argv[0])

  _file = open(s,"r")
  
  for line in _file:
    s = ' ssh -n %s "nohup available_hdd.py %s "> /dev/null 2>&1 &  ' %(line,line)
    thread.start_new_thread(os.popen(s))
    
   

if __name__ == '__main__':
  main(argv[1:])
