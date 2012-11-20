class ConfigureNetwork(object):
    def __init__(self, eth, ip, network, netmask, broadcast, gateway):
        self.eth = eth
        self.ip = ip
        self.netmask = netmask
        self.network = network
        self.gateway = gateway
        self.broadcast = broadcast
    def apply_values(self):
        raise NotImplementedError
    def restart_service(self):
        raise NotImplementedError

