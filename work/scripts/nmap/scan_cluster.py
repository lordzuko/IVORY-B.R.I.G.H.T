#!/usr/bin/python2

import os 
import sys
import commands as cmd

def main():
  op.popen("nmap -sP -n 192.168.0.0/24 | grep 192. | awk -F' ' '{print $5}' > nodes.txt")
  
  _file = open("nodes.txt")
  
  for ip in _file:
    if ip in ('192.168.0.103','192.168.0.254','192.168.0.250'):
      pass
    else:
      os.popen("")  
  

if __name__ == '__main__':
  main()

