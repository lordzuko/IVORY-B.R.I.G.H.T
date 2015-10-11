#!/usr/bin/python

"""
________________________________________________________________
|                                                              |
|                         CODED BY                             | 
|                                                              |
|                                                              | 
| 	     HIMANSHU MAURYA      BHAVISHYA MATHUR             |
|							       | 	
|______________________________________________________________|

"""

import os 
import sys
import set_jps

from sys import argv

"""__________________CLASS START's HERE_____________________________"""


class restart:
  # restart classes' constructor
  def __init__(self,arguments):
    self.rst(arguments)

  # controler function which taker as argument
  """
     f -->> format namenode
     n -->> restart namenode
     d -->> restart datanode
     j -->> restart jobtraker
     t -->> restart tasktracker
  """  

  def rst(self,arguments):

    for argu in arguments:
      # if argument is 'f' call format namenode
      if argu == 'f':
        self.format_namenode()
      # if argument is 'n' call restart namenode
      if argu == 'n':
        self.namenode_restart()
      # if argument is 'j' call restart jobtracker   
      if argu == 'j':
	self.jobtracker_restart()
      # if argument is 'd' call restart datanode
      if argu == 'd':
        self.datanode_restart()
      # if argument is 't' call restart tasktracker
      if argu == 't':
	self.tasktracker_restart()

# function to format namenode
    
  def format_namenode(self):    
    os.system("hadoop namenode -format")

# function to restart namenode

  def namenode_restart(self):
    os.system("hadoop-daemon.sh stop namenode")
    os.system("hadoop-daemon.sh start namenode")


# function to restart datanode
  def datanode_restart(self):
    os.system("hadoop-daemon.sh stop datanode")
    os.system("hadoop-daemon.sh start datanode")

# function to restart jobtracker

  def jobtracker_restart(self):
    os.system("hadoop-daemon.sh stop jobtracker")
    os.system("hadoop-daemon.sh start jobtracker")


# function to restart tasktracker
  def tasktracker_restart(self):
    os.system("hadoop-daemon.sh stop tasktracker")
    os.system("hadoop-daemon.sh start tasktracker")


""" ______________________________________________________________________"""

# main starts here

if __name__ == "__main__":
  rst =  restart(argv[1:])
   
  

