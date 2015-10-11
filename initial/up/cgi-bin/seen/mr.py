#!/usr/bin/python

import cgi
import cgitb
import os
import thread
import commands
cgitb.enable()

print "Content-type: text/html\n"

x='''<form action="process.py" method="POST">
	enter file_name with location: <input type="text" name="input" value="none"></br>or</br>
	select sample files: <select name="input_file">
				<option value="none"><---select a sample file---></option>
				<option value="/sample/file1.txt">file1</option>
				<option value="/sample/file1.txt">file2</option>
				<option value="/sample/file1.txt">file3</option>
			     </select></br>
	enter name of output folder: <input type="text" name="output" value="none"></br>
	<select name="mapper">
		<option value="none"><---Select a mapper---></option>
		<option value="mapper/m1.py">m1</option>       
	</select>
	<select name="reducer">
		<option value="none"><---Select a reducer---></option>
		<option value="wordcount">wordcount</option>
		<option value="reducer/mx_occ.py">max occurance</option>
		<option value="reducer/part_word.py">count particular word</option>       
	</select>
</br>

	enter word to count: <input type="text" name="word" value="none">
	</br><input type="submit" value="start">
	</form>'''

print x
