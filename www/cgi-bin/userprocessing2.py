#!/usr/bin/python2

import os
import sys
import commands as cmd
import time
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

username= form['name'].value
f_quota = form['f_quota'].value
s_quota = form['s_quota'].value

  
 
# check if /user directory is already present
if not os.system("sudo test -f /user"):
  os.popen("sudo hadoop fs -mkdir /user")
    
# check if /user/username directory is already present 
# if present that will mean user already exits 
if not os.system("sudo hadoop fs -mkdir /user/"+username):
  os.popen("sudo hadoop fs -chmod 777 /user/"+username)
  os.popen("sudo hadoop fs -chown "+username+" /user/"+username)	 
else:
  os.popen("echo 'user already exits' > /cgi-bin/log")
  
# check if spacequota is passed 'n' and 'c' as parameter -- > handle it separately
if s_quota == 'c' or s_quota == 'C':
  os.popen("sudo hadoop dfsadmin -clrSpaceQuota /user/"+username)
else:  
  if s_quota == 'n' or s_quota == 'N':
    pass
  else: 
    os.popen("sudo hadoop dfsadmin -setSpaceQuota "+s_quota+" /user/"+username)
    
# check if file quota is passed 'n' and 'c' as parameter -- > handle it separately
if f_quota == 'c' or f_quota == 'C':
  os.popen("sudo hadoop dfsadmin -clrQuota /user/"+username)
else:
  if f_quota == 'n' or f_quota == 'N':
    pass
  else: 
    os.popen("sudo hadoop dfsadmin -setQuota "+f_quota+" /user/"+username)  
    

print 'Content-type: text/html'
print 'location: http://192.168.5.53/UserConsole.html'
print '\n'
