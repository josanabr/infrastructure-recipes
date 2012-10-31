directory "/home/cluster/.ssh" do
	owner "cluster"
	group "admin"
	mode "0700"
	action :create
end

cookbook_file "/home/cluster/.ssh/authorized_keys" do
	source "id_rsa.pub"
	mode 0644
	owner "cluster"
	group "admin"
end
