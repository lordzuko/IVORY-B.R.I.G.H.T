#!/usr/bin/python2

import cgi
import os
import sys
import commands as cmd
import cgitb
cgitb.enable()

print 'Content-type: text/html'

print '\n'


#i have to generate this file 

# this file is in the following format

# <ip>:<hostname>:<hdd_available>:<slots_available>:<status>


os.system("hadoop fs -ls / > filelist.txt")

 


_file = open("fileslist.txt","r")

print '''
               		
			<div class="alert alert-info">
							<button type="button" class="close" data-dismiss="alert">x</button>
							<strong>Heads up!</strong> Please assign the job role to different nodes
						</div>
						
			</div>
		<div class="row-fluid sortable">		
				<div class="box span12">
					</div>
					<div class="box-content">
						<table class="table table-striped table-bordered bootstrap-datatable datatable">
						  <thead>
						  <tr>
								  <th>Permissions</th>
								  <th>replication</th>
								  <th>owner</th>
								  <th>group</th>
								  <th>size</th>
								  <th>date modified</th>
								  <th>time</th>
								  <th>file</th>
					         </tr>
      '''	
s  = _file.read()
s = s[:-2]
s = s.split('\n')
i=0
for line in s:
  ip = line.split(":")
  
  print "<tr>"
  print "<td>"+str(ip[0].strip(' '))+"</td>"  
  print	'<td class=\"center\" width= 30px>'+str(ip[1])+'</td>'
  print '<td width = \"30px\">'+ip[2]+'</td>' 
  print '<td class=\"center\" width = \"30px\">'+str(ip[3])+'</td>'  
  print '<td class=\"center\" width = \"70px\">'  
  print '<span class=\"label label-success\">'+str(ip[4])+'</span>'   
  print '</td>'
  print '<td class=\"center\">'+str(ip[5])+'</td>'
  print '<td class=\"center\">'+str(ip[6])+'</td>'
  print '<td class=\"center\">'+str(ip[7])'</td>'
  i=i+1
print '''
             					</tbody>
					  </table>            
					</div>
				</div><!--/span-->
				</div><!--/row-->
			

		
		
        '''


   
