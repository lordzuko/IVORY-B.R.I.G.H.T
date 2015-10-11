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
		<div class="row-fluid sortable" style="float:left;">		
				<div class="box span12">
					</div>
					<div class="box-content">
						<table class="table table-striped table-bordered bootstrap-datatable datatable">
						  <thead>
							  <tr>
							     <th>Files</th>
								  <th>Type</th>
								  <th>Replications</th>
								  <th>Blocksize</th>
							     <th>Actions</th>
							  </tr>
						  </thead>   
      '''	
s  = _file.read()
s = s[:-2]
s = s.split('\n')
for line in s:
  ip = line.split(":")
  s =  """ 					<tbody>
                                                        <tr>
								<td>%s</td>
								<td class="center">%s</td>
								<td class="center">%s</td>
								<td class="center">%s</td>
								<td class="center">									
								 <a class="btn btn-danger" href="#">
										<i class="halflings-icon white trash"></i> 
									</a>
								</td>
							</tr>
      
      
         """ % (ip[0].strip(' '),ip[1],ip[2],ip[3])
  print s

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


   
