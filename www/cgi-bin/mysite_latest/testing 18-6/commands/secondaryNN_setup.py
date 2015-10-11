#!/usr/bin/python2

import sys
import os


# chekpoint interval

'''
     USAGE : ./secondaryNN_setup.py   NN_IP:port  
 
'''

def main(argv):
  
  if len(argv) != 1:
    sys.exit("Usage ./secondaryNN_setup.py  NN_IP:port")
  
  s = "hdfs://"+argv[0]
  os.popen("sed -i 's/<\/configuration>/' /etc/hadoop/core-site.xml")
  _file = open("/etc/hadoop/core-site","a")
  p = '''
      
      '''

if __name__ == "__main__":
  main(argv[1:])
