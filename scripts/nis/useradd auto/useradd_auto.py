#!/usr/bin/python2

import os 
import sys

def main(argv):
  if len(argv) != 2:
    sys.exit("Usage ./useradd_auto <username> <password>")
  os.popen("useradd " + argv[0]) 
  os.popen("echo "+argv[1]+"|passwd "+argv[0]+" --stdin")
  
if __name__ == '__main__':
  main(sys.argv[1:])
