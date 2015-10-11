#!/usr/bin/python2

import os 
import sys
import commands as cmd
import time

# jobtracker_ip ,typeOfScheduler , include host, exclude host , minMap, MinReducer, MaxRunningJobs 

def main(argv):
  
  if len(argv) != 3:
    sys.exit("Usage mapred-site_modifier.py <tasktracker/jobtracker(T/J)> <jobtracker_ip> <FIFO/FAIR>")
  
  if os.system("rpm -q hadoop"):
    os.popen("yum install hadoop")
  
  os.popen("sed -i 's/<\/configuration>/ /' /etc/hadoop/mapred-site.xml")
    
  _file = open("/etc/hadoop/mapred-site.xml","a")
  
  if argv[0] == 'T':
    print argv[0]
    s = '''
           <property>
           <name>mapred.job.tracker</name>
           <value>%s:9002</value>
           </property>\n
        '''
    r = s %(str(argv[1]))
    
    _file.write(r)
    
  elif argv[0] == 'J':
    print argv[0]
    s = '''
           <property>
           <name>mapred.job.tracker</name>
           <value>%s:9002</value>
           </property>\n
        '''
    r = s %(str(argv[1]))
    _file.write(r)
    """ ------------------FAIR V/S FIFO--------------------------"""
    if argv[2] =='FIFO':
      pass
    elif argv[2] == 'FAIR':
      s = '''
              <property>
              <name>mapred.jobtracker.taskScheduler</name>
              <value>org.apache.hadoop.mapred.FairScheduler</value>
              </property>\n
            '''
      _file.write(s)
      
      s = '''
              <property>
              <name>mapred.fairscheduler.allocation.file</name>
              <value>/etc/hadoop/fair-scheduler.xml</value>
              </property>\n
            '''
  
      _file.write(s)
      
    """---------------------------------------------------------"""
  
  _file.write("</configuration>")
  _file.close()
  time.sleep(1)
if __name__ == '__main__':
  main(sys.argv[1:])
