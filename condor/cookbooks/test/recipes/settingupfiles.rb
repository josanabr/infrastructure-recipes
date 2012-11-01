cookbook_file "/etc/hosts" do
	source "hosts"
	mode 0755
	owner "condor"
	group "admin"
end

execute "hostname-stop" do
	user "root"
	group "admin"
	command "service hostname stop"
	action :run
        # http://help.opscode.com/discussions/problems/732-bash-non-zero-exit-status
	returns 1
end

template "/etc/hostname" do
	source "hostname.erb"
	mode 0644
	owner "root"
	group "admin"
	variables(
		:hostname_ => "#{node[:host_name]}"
	)
end

execute "hostname-start" do
	user "root"
	group "admin"
	command "service hostname start"
	action :run
end

cookbook_file "/var/tmp/condor.tar.gz" do
	source "condor.tar.gz"
	mode 0444
	owner "condor"
	group "admin"
end

execute "tar" do
	user "condor"
	group "admin"
	cwd "/tmp"
	command "tar xfz /var/tmp/condor.tar.gz"
	action :run
end

cookbook_file "/tmp/condor/install.bash" do
	source "install.bash"
	mode 0755
	owner "condor"
	group "admin"
end
