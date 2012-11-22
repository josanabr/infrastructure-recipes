# 
# How to use this class
#
# s = SFTPCopy("ssh://josanabr@localhost:22")
# s.copy("/home/josanabr/temp.png","/tmp/otro.png")
# s.close()
#
import os
import paramiko
import socket 
import sys
from urlparse import urlparse
from fancy import cyclic

class SFTPCopy:
	def __init__(self, sshurl):
		u = urlparse(sshurl)
		self.username = u.username
		self.hostname = u.hostname
		self.port = u.port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.socket.connect((self.hostname, self.port))

	def connect_via_pkey(self):
		self.t = paramiko.Transport(self.socket)
		self.t.start_client()
		privatekeyfile = os.path.expanduser("~/.ssh/id_rsa")
		mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
		self.t.auth_publickey(self.username,mykey)
		self.sftp = paramiko.SFTPClient.from_transport(self.t) 

	def copy(self, source, dest):
		self.connect_via_pkey()
		self.sftp.put(source, dest, callback=printTotals)

	def close(self):
		self.sftp.close()
		self.t.close()

def printTotals(transferred, toBeTransferred):
	if transferred%8192 == 0: 
		sys.stdout.write("\r%c"%cyclic()) 
		sys.stdout.flush()
		
def copyViaSSH(ssh_url, source, remote_target):
	sftp = SFTPCopy(ssh_url)
	sftp.copy(source, remote_target)
	sys.stdout.write("\n") 
	sys.stdout.flush()
	sftp.close()

