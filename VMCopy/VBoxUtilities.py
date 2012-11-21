import os
import re
from SFTPCopy import *

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

vm_str = "cloudera hadoop"
ssh_url = "ssh://josanabr@localhost:22"
remote_dir = "/tmp"
exportVM(vm_str)
copyViaSSH(ssh_url,"%s.ova"%vm_str,"%s/%s.ova"%(remote_dir,vm_str))


# Check if a required vm is runnig
# if so -> stop it
# Export vm
# Copy to the  remote center
# To the remote center import it
# Modify its network interfaces in such a way that it could be attached to remote network interfaces
