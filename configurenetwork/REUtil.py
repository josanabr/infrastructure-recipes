# Usage mode
# 	python REUtil.py -a 192.118.15.20 -i eth1 -n 192.118.0.0 -m 255.255.0.0 -b 192.118.255.255 -g 192.118.0.1 -f interfaces
import re
import time
import argparse
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

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Network filename e.g. interfaces")
parser.add_argument("-a","--address", help="IP address")
parser.add_argument("-i","--interface", help="Network interface e.g. eth0, eth1, ...")
parser.add_argument("-n","--network", help="Network address")
parser.add_argument("-b","--broadcast", help="Broadcast address")
parser.add_argument("-g","--gateway", help="Gateway address")
parser.add_argument("-m","--netmask", help="Network mask e.g. 255.255.0.0")
args = parser.parse_args()

appendEthEntry(args.filename, args.interface, args)
