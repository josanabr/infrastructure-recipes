# This script modifies the default network configuration defined by Vagrant.
# A VM created with Vagrant goes to Internet through eth0(NAT) interface.
# For reducing latency this recipe changes the default route to a local proxy. 
# 
# The interfaces file is changed in such a way that interface eth1 
# be used to surf to Internet.
template "/etc/network/interfaces" do
	source "interfaces.erb"
	mode 0644
	owner "root"
	group "root"
	variables(
		:my_ip => "#{node[:my_ip]}",
		:my_gateway => "#{node[:my_gateway]}",
		:my_netmask => "#{node[:my_netmask]}"
	)
end
# The dns entry is also changed.
template "/etc/resolv.conf" do
	source "resolv.conf.erb"
	mode 0644
	owner "root"
	group "root"
	variables(
		:my_dns => "#{node[:my_dns]}"
	)
end
# Remove NAT as default route
execute "routedelete" do
	user "root"
	group "root"
	command "/sbin/route del default"
	action :run
end
# Restart the networking service for incorporating the new changes
execute "networking" do
	user "root"
	group "root"
	command "/etc/init.d/networking restart"
	action :run
end
