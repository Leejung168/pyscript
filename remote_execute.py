import paramiko
import getpass
import threading
# un = input('Enter your username: ')
# pw = getpass.getpass('Enter your password: ')
# hosts = ['54.65.214.115','54.65.214.115']

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


if __name__ == '__main__':
    hs = input('Enter your hosts: ')
    hosts = hs.split(",")
    un = 'ec2-user'
    pw = 'leejung168'
    cmd = input('Enter the command: ')
    s = threading.BoundedSemaphore(3)
    T = []
    for h in hosts:
        s = ssh(cmd, host=h)
        print("================The server {0} is running======>commands: {1}: ================".format(h,cmd))
        t = threading.Thread(target=s.login(), name=h).start()
        T.append(t)

