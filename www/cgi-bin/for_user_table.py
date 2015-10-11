#!/usr/bin/python2

import cgi
import os
import sys
import commands as cmd
import cgitb
cgitb.enable()
import time
print 'Content-type: text/html'

print '\n'


#i have to generate this file 

# this file is in the following format

# <ip>:<hostname>:<hdd_available>:<slots_available>:<status>

 
#os.popen("python filelistgen.py");


_file = open("userlist.txt","r")

print '''	
		<div class="row-fluid sortable" style="float:left;">		
				<div class="box span12">
					</div>
					<div class="box-content">
						<table class="table table-striped table-bordered bootstrap-datatable datatable">
						  <thead>
							  <tr>
							     <th>User Name</th>
						             <th>User Directory</th>
							     <th>Actions</th>
							  </tr>
						  </thead>   
      '''	
s  = _file.read()
s = s[:-2]
s = s.split('\n')
i=0
for line in s:
  ip = line.split(":")
  print "<tbody>"
  print "<tr>"
  
  print "<tr><td name=\'uname"+str(i)+"\'>"+ip[0]+"</td>"
  print "<td class=\"center\" name=\'dir"+str(i)+"\'>"+ip[1]+"</td>"
  print "<td class=\'center\'>"
  print "<a class=\'btn btn-info black\' href=\'http://192.168.5.53/cgi-bin/userprocessing1.py?uname"+str(i)+"="+ip[0]+"&dir"+str(i)+"="+ip[1]+"\'>"
  print "<i class=\'halflings-icon white ban-circle\'></i></a>" 									
  print "<a class=\'btn btn-danger\' href=\'http://192.168.5.53/cgi-bin/userprocessing1.py?uname"+str(i)+"="+ip[0]+"&dir"+str(i)+"="+ip[1]+"\'>"
  print "<i class=\'halflings-icon white trash\'></i>" 
  print "</a>"
															
  print "</td>"
  print "</tr>"
		      

print '''
             					</tbody>
					  </table>            
					</div>
				</div><!--/span-->
				</div><!--/row-->
			
				</div><!--/span-->

			</div><!--/row-->
		
		
        '''


   
