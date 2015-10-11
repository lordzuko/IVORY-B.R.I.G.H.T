#!/usr/bin/python2

import os
import sys
import commands as cmd
import time

while True:
  _file = open("/var/www/html/mysite_latest/serverload.txt","w")
  server_idle=float(os.popen("iostat | head -4| tail -1 | awk '{print $6}'").read().strip())
  server_load = float(100) - server_idle
  _file.write(server_load)
  _file.close()
  time.sleep(4)

#prints float value
