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

 
print '<h1> hello </h1>'

_file = open("nodeInfo.txt","r")

print '''
		<div class="row-fluid sortable">		
				<div class="box span12">
					</div>
					<div class="box-content">
						<table class="table table-striped table-bordered bootstrap-datatable datatable">
						  <thead>
						  <tr>
								  <th>IP</th>
								  <th>Hostname</th>
								  <th>Available HDD</th>
								  <th>Available Slots</th>
								  <th>Status</th>
								  <th>Actions</th>
					         </tr>
      '''	
s  = _file.read()
s = s[:-2]
s = s.split('\n')
for line in s:
  ip = line.split(":")
  s =  """
                                                        <tr>
	     							<td>%s</td>  
								<td class="center">%s</td>
								<td>%s</td> 
								<td class="center">
								<td>%s</td>  
								<td class="center">  
									<span class="label label-success">%s</span>   
								</td>
									<div class="control-group">
								<!--<label class="control-label" for="selectError1">Multiple Select / Tags</label>-->
								<div class="controls">
								  <select id="selectError1" multiple data-rel="chosen">
									<option>Namenode</option>
									<option>Datanode</option>
									<option>Job Tracker</option>
									<option>Task Tracker</option>
									<option>Secondary Namenode</option>
									<option>Backup Namenode</option>
								  </select>
								</div>
							  </div>
								</td>
							</tr>
      
      
         """ % (ip[0],ip[1],ip[2],ip[3],ip[4])
  print s

print '''
             					</tbody>
					  </table>            
					</div>
				</div><!--/span-->
				</div><!--/row-->
        '''


   
