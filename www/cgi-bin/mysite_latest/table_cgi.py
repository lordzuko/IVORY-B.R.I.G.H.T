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
								  <th>Actions</th>
					         </tr>
      '''	
s  = _file.read()
s = s[:-2]
s = s.split('\n')
i=0
for line in s:
  ip = line.split(":")
  s =  """
                                                        <tr>
	     							<td>%s</td>  
								<td class="center" width= 30px> %s</td>
								<td width = "30px">%s</td> 
								<td class="center" width = "30px">%s</td>  
								<td class="center" width = "7	0px">  
									<span class="label label-success">%s</span>   
								</td>
                                                                <td class="center">
								<div class="control-group">
								<div class="controls">""" % (ip[0].strip(' '),ip[1],ip[2],ip[3],ip[4])
  
  print s
  print '<select id=\"selectError1\" multiple data-rel=\"chosen\" name=\"multi'+str(i)+'\">'
  print """	<option>Namenode</option>
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
      
      
         """ 

print '''
             					</tbody>
					  </table>            
					</div>
				</div><!--/span-->
				</div><!--/row-->
			<div class="form-actions">
							  <button type="submit" class="btn btn-primary">Save changes</button>
							  <button type="reset" class="btn">Cancel</button>
							</div>
						  </fieldset>
						</form>   

					</div>
				</div><!--/span-->

			</div><!--/row-->
		
		
        '''


   
