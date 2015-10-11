#!/usr/bin/python2

import os
import sys
from sys import argv
class nfs:
  def __init__(self,arguments):
    self.nfs_driver(arguments)
  

  def nfs_driver(self,argv):
    arg_sp=argv.split('-')
    arr=[]
    c=0
    for i in arg_sp:
      c+=1
      arr.insert(c,i.split())
    c=1
    s=""
    for i in range(0,len(arr)):
      if arr[i][0] == "dir":
        s+=arr[i][1]
      if arr[i][0] == "ip":
        s+=" "+arr[i][1]
      if arr[i][0]=="perm":
        if arr[i][1]==1:
           s+="(rw,sync)"
        elif arr[i][1]==2:
           s+="(ro,sync)"
        elif arr[i][1]==3:
           s+="(rw,no_root_squash)"
        elif arr[i][1]==4:
           s+="(rw,root_squash)"
    f=open("/etc/exports","a")
    f.write(s)
    f.close()

if __name__ == "__main__":
  nfs_obj = nfs(argv[1:])
       
