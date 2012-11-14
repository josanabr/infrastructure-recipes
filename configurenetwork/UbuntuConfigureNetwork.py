from ConfigureNetwork import *

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

x = UbuntuConfigureNetwork('eth0','192.168.28.57','255.255.255.0','192.168.28.0','192.168.28.1','192.168.28.255')
print x

