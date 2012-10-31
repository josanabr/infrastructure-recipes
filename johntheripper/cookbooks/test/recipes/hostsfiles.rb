# hostname file is created
template "/etc/hostname" do
	source "hostname.erb"
	mode 0644
	owner "root"
	group "root"
	variables(
		:hostname => "#{node[:john_hostname]}"
	)
end
# hosts file is created from a template file
cookbook_file "/etc/hosts" do
	source "hosts"
	mode 0644
	owner "root"
	group "root"
end
# the hostname service is restarted
execute "hostname" do
	user "root"
	group "root"
	command "/etc/init.d/hostname restart"
	action :run
end
