# Usage mode
# 	python UbuntuConfigureNetwork.py -a 192.118.15.20 -i eth1 -n 192.118.0.0 -m 255.255.0.0 -b 192.118.255.255 -g 192.118.0.1 -f interfaces
import argparse
from ConfigureNetwork import *
from REUtil import *

class UbuntuConfigureNetwork(ConfigureNetwork):
	""" 
This class deals with the modification of the /etc/network/interfaces 
configuration file.
This class scans the interfaces file and finds a line containing the following pattern
	auto self.eth
	iface self.eth
From that point on afterward, it starts removing the lines coming next until another line starting with auto or iface is found.
	"""
	configure_network = "/etc/network/interfaces"
	def apply_values(self): 
		return
	def __str__(self): 
		return ' eth: %s \n IP: %s \n Netmask: %s \n Network: %s \n Gateway: %s \n Broadcast: %s' % (self.eth, self.ip, self.netmask, self.network, self.gateway, self.broadcast)
    	def remove_auto_entry(self, _file, eth):
		pattern = "^auto %s.*"%eth
		removeLineWithPattern(_file, pattern)
    	def remove_iface_entry(self, _file, eth):
		pattern = "^iface %s.*"%eth
		self.remove_auto_entry(_file, eth)
		removeLinesFromPattern1ToPattern2(_file,pattern,r"^iface.*|^auto.*|\n+")
	def apply_values(self, _file):
		appendEthEntry(_file, self.eth, self.ip, self.network, self.netmask, self.broadcast, self.gateway)


parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Network filename e.g. interfaces")
parser.add_argument("-a","--address", help="IP address")
parser.add_argument("-i","--interface", help="Network interface e.g. eth0, eth1, ...")
parser.add_argument("-n","--network", help="Network address")
parser.add_argument("-b","--broadcast", help="Broadcast address")
parser.add_argument("-g","--gateway", help="Gateway address")
parser.add_argument("-m","--netmask", help="Network mask e.g. 255.255.0.0")
args = parser.parse_args()

x = UbuntuConfigureNetwork(args.interface,args.address,args.network,args.netmask,args.broadcast,args.gateway)
x.apply_values(args.filename)
print x
