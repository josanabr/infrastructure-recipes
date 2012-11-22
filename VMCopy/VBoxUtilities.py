import os
import re
from SFTPCopy import *
from SSHCmd import *
from fancy import *

VBoxSK = "VBoxManage"

def vmExists(vm):
	pattern = "^\"*%s\".*"%vm
	stream = os.popen("%s list vms"%VBoxSK)
	for i in stream:
		matchObj = re.match(pattern, i)
		if matchObj:
			return True
	return False
	
def vmIsRunning(vm):
	pattern = "^\"*%s\".*"%vm
	stream = os.popen("%s list runningvms"%VBoxSK)
	for i in stream:
		matchObj = re.match(pattern, i)
		if matchObj:
			return True
	return False

def stopVM(vm):
	command = "%s controlvm \"%s\" poweroff"%(VBoxSK,vm)
	returned = os.system(command)
	if returned != 0:
		print "Error stopping \"%s\""%vm
		return False
	return True

def exportVM(vm):
	print "Exporting..."
	if not vmExists(vm):
		print "\"%s\" vm does not exist\n"%vm
		return False
	else:
		print "Machine does exist"
	if vmIsRunning(vm):
		print "Machine is running"
		if stopVM(vm):
			if os.system("%s export \"%s\" -o \"%s\".ova"%(VBoxSK,vm,vm)) != 0:
				print "Error exporting \"%s\""%vm
				return False
			return True
	else:
		if os.system("%s export \"%s\" -o \"%s\".ova"%(VBoxSK,vm,vm)) != 0:
			print "Error exporting \"%s\""%vm
			return False
		return True
		
	return False

vm_str = "tmp_1353453240"
ssh_url = "ssh://clouduser@192.168.28.57:22"
remote_dir = "/tmp"
remote_file = "%s/%s.ova"%(remote_dir,vm_str)
# Check if a required vm is runnig
# if so -> stop it
# Export vm
#print "Exporting vm: %s"%vm_str
#exportVM(vm_str)
# Copy to the  remote center
#print "Copying"
#copyViaSSH(ssh_url,"%s.ova"%vm_str, remote_file)
# To the remote center import it
#print "Importing to the remote site"
#ret_code = execute_ssh_command(ssh_url,"/usr/bin/VBoxManage import %s"%remote_file)


# Modify its network interfaces in such a way that it could be attached to remote network interfaces
