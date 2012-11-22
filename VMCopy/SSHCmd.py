# 
# How to use this class
#
# s = SSHCmd("ssh://josanabr@localhost:22")
# print s.execute_cmd("ls -l")
#
import paramiko
from urlparse import urlparse
from fancy import cyclic
import time
import sys

class SSHCmd:
	def __init__(self, sshurl): 
		u = urlparse(sshurl)
		self.username = u.username
		self.hostname = u.hostname
		self.port = u.port
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	def connect(self):
		self.client.connect(self.hostname, port=self.port, username=self.username)
	def execute_cmd(self, cmd):
		self.connect()
		chan = self.client.get_transport().open_session()
		chan.exec_command(cmd)
		while not chan.exit_status_ready():
			sys.stdout.write("\r%c"%cyclic())
			sys.stdout.flush()
			time.sleep(0.8)
		self.client.close()
		sys.stdout.write("\n") 
		sys.stdout.flush()
		return chan.recv_exit_status()

def execute_ssh_command(ssh_url, cmd):
	s = SSHCmd(ssh_url)
	return s.execute_cmd(cmd)
