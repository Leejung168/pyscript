#!/usr/bin/env python
import re,os
from sys import argv
script, src, des = argv
HOST = []
HOSTNAME = []
PORT = []
with open(src) as f:
    for line in f:
        if re.search("^host", line):
            HOST.append(line.split().pop())
        if re.search("hostname", line):
            HOSTNAME.append(line.split().pop())
        if re.search("port", line):
            PORT.append(line.split().pop())

entry = zip(HOST,HOSTNAME,PORT)
with open(des, 'a') as w:
    for e in entry:
        w.write(e[0] + " " + "ansible_ssh_host=" + e[1] + " " + "ansible_ssh_port=" + e[2] + '\n')
