#!/usr/bin/python2


#f  = open('/etc/passwd')

import sys

for i in sys.stdin:
  print i.strip('\n') 
