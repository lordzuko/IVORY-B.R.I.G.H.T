#!/usr/bin/python2

import os 
import sys
import commands as cmd

def main(argv):
  """ IF heartBeat --> n -->> heatBeat set as Default """
  
  if len(argv) != 4:
    sys.exit("Usage ./hdfs-site_modifier.py  <datanode(D)/namenode(N)> <heartBeat> <rep_factor> <blk_size>")
  
  if not os.system("rpm -q hadoop"):
    os.popen("yum install hadoop")
  
  os.popen("sed -i 's/<\/configuration>/./' /etc/hadoop/hdfs-site.xml")
    
  _file = open("hadoop/hdfs-site.xml","a")

  if argv[0] == 'D'  
    s = '''
           <property>
           <name>dfs.data.dir</name>
           <value>/HBS_datanode</value>
           </property>\n
        '''
    _file.write(s)
  
  
    """____________________________________________________"""
  
                   """ HEART BEAT """
    """____________________________________________________"""
    if argv[1] == 'n':
      pass
    else:
      s = '''
            <property>
            <name>dfs.heartbeat.interval</name>
            <value>%s</value>
            </property>
          '''
  
    
      r = '%s\n' % (s % ''.join(str(argv[1])))
  
      _file.write(r)

  elif argv[0] == 'N':
    s = '''
           <property>
           <name>dfs.name.dir</name>
           <value>/HBS_namenode</value>
           </property>\n
        '''
    _file.write(s)  
    
    """____________________________________________________"""
  
                   """ REPLICATION FACTOR """
    """____________________________________________________"""

    if argv[2] =='n':
      pass
    else
      s = '''
            <property>
            <name>dfs.replication</name>
            <value>%s</value>
            </property>
          '''
      r = '%s\n' % (s % ''.join(str(argv[2])))
  
      _file.write(r)

    """____________________________________________________"""
  
                   """ BLOCK SIZE """
    """____________________________________________________"""

    if argv[3] =='n':
      pass
    else
      s = '''
            <property>
            <name>dfs.block.size</name>
            <value>%s</value>
            </property>
          '''
      r = '%s\n' % (s % ''.join(str(argv[3])))
  
      _file.write(r)


    """----------------------------------------------------"""

  _file.write("</configuration>")
  _file.close()

if __name__ == '__main__':
  main(sys.argv[1:])
