#!/usr/bin/python2

import os 
import sys
import commands as cmd

def main():
  #os.popen("mkdir  -p /root/Desktop/testing/hadoop_setup")
  os.popen("nmap -sP -n 192.168.0.0/24 | grep 192. | awk -F' ' '{print $5}' > nodes")

if __name__ == '__main__':
  main()

