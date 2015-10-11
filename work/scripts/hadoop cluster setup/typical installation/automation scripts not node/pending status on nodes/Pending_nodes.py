#!/usr/bin/python2

import os
import sys

s="diff -n --rcs ssh.txt nodes.txt | grep 192."
s=os.popen(s+" > pendingstatus.txt").read()

