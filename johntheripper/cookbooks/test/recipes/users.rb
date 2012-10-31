# User is created
user "cluster" do
	not_if "id cluster"
	comment "Cluster user"
	uid 600
	gid "admin"
	home "/home/cluster"
	password "$1$ZFLDhbwu$5sa39wH60W/NyQYAKy2xV0" # Password: gridadmin
	shell "/bin/bash"
	supports :manage_home => true
end

# a new directory where additional binaries would be installed is created
directory "/home/cluster/bin" do
	owner "cluster"
	group "admin"
	mode "0755"
	action :create
end

# a customized profile file is copied in user's directory. 
# It adds the ${HOME}/bin directory to the ${PATH} variable
template "/home/cluster/.profile" do
	source "profile.erb"
	mode 0666
	owner "cluster"
	group "admin"
end
