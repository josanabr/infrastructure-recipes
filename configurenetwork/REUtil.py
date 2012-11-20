import re
import time
import os

def timeInMillis():
	return int(round(time.time() * 1000))

def removeLinesFromPattern1ToPattern2(_file,pattern1, pattern2):
	try:
		inputFile = open(_file,"r")
	except IOError:
		print "File not found"
		return ""
	temporaryFilename = _file + "." + str(timeInMillis())
	temporaryFile = open(temporaryFilename,"w")
	found = False
	# Identify if pattern is matched
	while True:
		line = inputFile.readline()
		if not line:
			break
		matchObj = re.match(pattern1, line)
		if matchObj: # Pattern matched
			found = True
			break
		temporaryFile.write(line)
	if found: # when pattern is matched
		  # remove all lines from there to pattern2
		while True:
			line = inputFile.readline()
			if not line:
				break
			matchObj = re.match(pattern2, line)
			if matchObj: #pattern2 is found
				break
		if line: # it should be included on the resulting file
			temporaryFile.write(line)
		while True: # add final lines coming from original file
			line = inputFile.readline()
			if not line:
				break
			temporaryFile.write(line)
	inputFile.close()
	temporaryFile.close()
	copy(_file,temporaryFilename)
	os.remove(temporaryFilename)
			
def removeLineWithPattern(_file,pattern1):
	try:
		inputFile = open(_file,"r")
	except IOError:
		print "File not found"
		return ""
	temporaryFilename = _file + "." + str(timeInMillis())
	temporaryFile = open(temporaryFilename,"w")
	while True:
		line = inputFile.readline()
		if not line:
			break
		matchObj = re.match(pattern1,line)
		if matchObj:
			continue
		else:
			temporaryFile.write(line)
	inputFile.close()
	temporaryFile.close()
	copy(_file,temporaryFilename)
	os.remove(temporaryFilename)

def copy(filetgt, filesrc):
	try:
		file1 = open(filesrc,"r")
	except IOError:
		print "File not found"
		return ""
	file2 = open(filetgt,"w")
	while True:
		line = file1.readline()
		if not line:
			break
		file2.write(line)
	file1.close()
	file2.close()

def appendLine(_file,line):
	try:
		file1 = open(_file,"a")
	except IOError:
		print "File not found"
		return ""
	file1.write(line)
	file1.close()

def writeNetworkIFFileEntries(_file,args):
	try:
		file1 = open(_file,"a")
	except IOError:
		print "File not found"
		return ""
	file1.write( "auto %s\n"%args.interface )
	file1.write( "iface %s inet static\n"%args.interface )
	file1.write( "\taddress %s\n"%args.address )
	file1.write( "\tnetwork %s\n"%args.network )
	file1.write( "\tnetmask %s\n"%args.netmask )
	file1.write( "\tbroadcast %s\n"%args.broadcast )
	file1.write( "\tgateway %s\n"%args.gateway )
	file1.close()
def appendEthEntry(_file,eth,args):
	pattern = "^auto %s.*"%eth
	removeLineWithPattern(_file,pattern)
	pattern = "^iface %s.*"%eth
	removeLinesFromPattern1ToPattern2(_file,pattern,r"^iface.*|^auto.*|\n+")
	writeNetworkIFFileEntries(_file,args)

def writeNetworkIFFileEntries(_file, eth, address, network, netmask, broadcast, gateway):
	try:
		file1 = open(_file,"a")
	except IOError:
		print "File not found"
		return ""
	file1.write( "auto %s\n"%eth )
	file1.write( "iface %s inet static\n"%eth )
	file1.write( "\taddress %s\n"%address )
	file1.write( "\tnetwork %s\n"%network )
	file1.write( "\tnetmask %s\n"%netmask )
	file1.write( "\tbroadcast %s\n"%broadcast )
	file1.write( "\tgateway %s\n"%gateway )
	file1.close()
def appendEthEntry(_file, eth, address, network, netmask, broadcast, gateway):
	pattern = "^auto %s.*"%eth
	removeLineWithPattern(_file,pattern)
	pattern = "^iface %s.*"%eth
	removeLinesFromPattern1ToPattern2(_file,pattern,r"^iface.*|^auto.*|\n+")
	writeNetworkIFFileEntries(_file, eth, address, network, netmask, broadcast, gateway)
