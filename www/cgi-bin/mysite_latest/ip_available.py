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

 


_file = open("nodeInfo.txt","r")

print '''
                
		<fieldset>
			
										<div class="row-fluid">
			<div class="alert alert-info">
							<button type="button" class="close" data-dismiss="alert">x</button>
							<strong>Heads up!</strong> Nodes in Cluster
						</div>
						
			</div>
		<div class="row-fluid sortable">		
				<div class="box span12">
					</div>
					<div class="box-content">
						<table class="table table-striped table-bordered bootstrap-datatable datatable">
						  <thead>
						  <tr>
								  <th>IP</th>
								  <th>Hostname</th>
								  <th>HDD</th>
								  <th>Slots</th>
								  <th>Status</th>
								  
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
  print '<td class=\"center\">'
  print '<div class=\"control-group\">'
  print '<div class=\"controls\">'
  
  
 
print '''
             					</tbody>
					  </table>            
					</div>
				</div><!--/span-->
				</div><!--/row-->
			
		
		
        '''


   
