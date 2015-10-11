#!/usr/bin/python
import sys
import os
def main(argv):
  
  # if spacequota == n -->  space quota not applicable
  # if spacequota == c --> clear space quota
  # if filequota == n --> file quota not applicable
  # if filequota == c --> clear file quota
  
  if len(argv) != 3:
    sys.exit("Usage ./user_quota username spacequota filequota")
  
  username = argv[0]  
 
  # check if /user directory is already present
  if not os.system("test -f /user"):
    os.popen("hadoop fs -mkdir /user")
    
  # check if /user/username directory is already present 
  # if present that will mean user already exits 
  if not os.system("hadoop fs -mkdir /user/"+username):
    os.popen("hadoop fs -chmod o-rwx /user/"+username)	 
  else:
    sys.exit("user already exits")
  
  # check if spacequota is passed 'n' and 'c' as parameter -- > handle it separately
  if argv[1] == 'c' or argv[1] == 'C':
    os.popen("hadoop dfsadmin -clrSpaceQuota /user/"+username)
  else:  
    if argv[1] == 'n' or argv[1] == 'N':
      pass
    else: 
      os.popen("hadoop dfsadmin -setSpaceQuota "+argv[1]+" /user/"+username)
    
  # check if file quota is passed 'n' and 'c' as parameter -- > handle it separately
  if argv[2] == 'c' or argv[2] == 'C':
    os.popen("hadoop dfsadmin -clrQuota /user/"+username)
  else:
    if argv[2] == 'n' or argv[2] == 'N':
      pass
    else: 
      os.popen("hadoop dfsadmin -setQuota "+argv[2]+" /user/"+username)  
    

if __name__ == "__main__":
  main(sys.argv[1:])  
