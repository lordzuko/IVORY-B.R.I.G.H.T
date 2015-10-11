#!/usr/bin/python2

import os 
import sys
import commands as cmd


# jobtracker_ip ,typeOfScheduler , include host, exclude host , minMap, MinReducer, MaxRunningJobs 

def main(argv):
  
  if len(argv) != 3:
    sys.exit("Usage ./mapred-site_modifier.py <tasktracker/jobtracker(T/J)> <jobtracker_ip> <FIFO/FAIR>")
  
  if not os.system("rpm -q hadoop"):
    os.popen("yum install hadoop")
  
  os.popen("sed -i 's/<\/configuration>/./' /etc/hadoop/mapreds-site.xml")
    
  _file = open("hadoop/mapred-site.xml","a")
  
  if argv[0] == 'T':
    s = '''
           <property>
           <name>mapred.job.tracker</name>
           <value>%s:9002</value>
           </property>
        '''
    r = '%s\n' %(str(argv[1]))

    _file.write(r)
  elif argv[0] == 'J':
    
    s = '''
           <property>
           <name>mapred.job.tracker</name>
           <value>%s:9002</value>
           </property>
        '''
    r = '%s\n' %(str(argv[1]))
    
    """ ------------------FAIR V/S FIFO--------------------------"""
    if argv[2] =='FIFO':
      pass
    elif argv[2] == 'FAIR':
      s = '''
              <property>
              <name>mapred.fairscheduler.allocation.file</name>
              <value>/etc/hadoop/fair-scheduler.xml</value>
              </property>
            '''
  
      _file.write(s)
    """---------------------------------------------------------"""
  
  _file.write("</configuration>")
  _file.close()
  
if __name__ == '__main__':
  main(sys.argv[1:])
