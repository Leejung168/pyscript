#!/usr/bin/env python3.4
# This script can help you to run command on remote server
# hosts = ['54.65.214.115','54.65.214.115']

import paramiko
import getpass
import threading
from queue import Queue
# un = input('Enter your username: ')
# pw = getpass.getpass('Enter your password: ')
q = Queue()
e = threading.Event()

class ssh():
    def __init__(self, cmd, host='54.65.214.115', port=40022):
        self.host = host
        self.username = un
        self.password = pw
        self.port = port
        self.cmd = cmd
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def login(self):
        self.client.connect(self.host, username=self.username, password=self.password, port=self.port,timeout=5)
        stdin, stdout, stderr = self.client.exec_command(self.cmd)
        for o in stdout:
            print(o)
        print("---------------Done----------------Done----------------Done-----------------")

def instance():
    while not e.is_set():
        message = q.get()
        s = ssh(cmd, host=message)
        t = threading.Thread(target=s.login(), name=message).start()
        if q.empty():
            e.set()
def wrap(m):
    with m:
        instance()
if __name__ == '__main__':
    un = input('Enter your username: ')
    pw = getpass.getpass('Enter your password: ')
    cmd = input('Enter the command: ')
    hs = input('Enter your hosts: ')
    hosts = hs.split(",")
    for x in hosts:
        q.put(x)
    m = threading.BoundedSemaphore(len(hosts))
    for x in (range(len(hosts))):
        threading.Thread(target=wrap, args=(m,), name='worker-{0}'.format(x)).start()




