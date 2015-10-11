#!/usr/bin/python2

import sys
import signal



def lw():
	print "bye"
	exit()


str = raw_input("enter us data:")

for x in str:
	print x


signal(2,lw())
