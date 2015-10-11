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
from sys import argv

"""__________________CLASS START's HERE_____________________________"""


class MRexample:
  # MRexample classes' constructor
  def __init__(self,arguments):
    self.example(arguments)

  # controler function which taker as argumen

  def example(self,arguments):

    for argu in arguments:
      # if argument is 'wordcount' call wordcount count function 
      if argu == 'wordcount':
        self.wordcount()
      
# function to run the example job    
  def wordcount(self):    
    filename=raw_input("Enter the file to be processed >")
    output_folder= raw_input("Enter the \"UNIQUE \" output folder>") 
    os.system("hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount "+filename+" "+output_folder+"")
""" ______________________________________________________________________"""

# main starts here

if __name__ == "__main__":
  example =  MRexample(argv[1:])
   
  

