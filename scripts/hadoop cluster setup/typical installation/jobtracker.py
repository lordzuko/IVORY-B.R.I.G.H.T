#!/usr/bin/python2

import os
import sys
import commands as cmd

def main(argv):
  
  if len(argv) == 3:
    sys.exit("./jobtracker.py <namenode_ip> <jobtracker_ip> <FAIR/FIFO>")
  
  #changes made in /etc/hadoop/mapred-site.xml
  os.popen("./mapred-site_modifier.py J "+ argv[1]+" "+argv[2])
  
  #changes made in /etc/hadoop/core-site.xml
  os.popen("./core-site_modifier.py "+argv[0]+" n")
  
  os.popen("hadoop-daemon.sh start jobtracker")
  status,output = cmd.getstatusoutput("/usr/java/jdk1.7.0_51/bin/jps | grep JobTracker | awk -F' ' '{print$2}'")
  
  if output == 'JobTracker':
    pass
  else:
    sys.exit("JobTracker not started!!")

if __name__=='__main__':
  main(sys.argv[1:])
