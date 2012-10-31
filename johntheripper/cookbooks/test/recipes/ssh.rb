directory "/home/cluster/.ssh" do
	owner "cluster"
	group "admin"
	mode "0700"
	action :create
end

cookbook_file "/home/cluster/.ssh/id_rsa" do
	source "id_rsa"
	mode 0600
	owner "cluster"
	group "admin"
end

cookbook_file "/home/cluster/.ssh/id_rsa.pub" do
	source "id_rsa.pub"
	mode 0644
	owner "cluster"
	group "admin"
end
