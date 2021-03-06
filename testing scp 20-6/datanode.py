#!/usr/bin/python2

import os
import sys
import commands as cmd
import time
def main(argv):
  if len(argv) != 2:
    sys.exit("Usage datanode.py <namenode_ip> <heart_beat>")
  
  #changes made in /etc/hadoop/hdfs-site.xml 
  os.popen("hdfs-site_modifier.py D "+argv[1]+" n n")
  #changes made in /etc/hadoop/core-site.xml
  os.popen("core-site_modifier.py "+argv[0]+" n")
  
  os.popen("hadoop-daemon.sh start datanode")
  time.sleep(5)
  status,output = cmd.getstatusoutput("/usr/java/jdk1.7.0_51/bin/jps | grep DataNode | awk -F' ' '{print$2}'")
  
  if output == 'DataNode':
    pass
  else:
    sys.exit("DataNode not started!!")

if __name__=='__main__':
  main(sys.argv[1:])
