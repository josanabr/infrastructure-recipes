template "/home/cluster/.mpd.conf" do
	source "mpd.erb"
	mode 0600
	owner "cluster"
	group "admin"
	variables(
		:password => "#{node[:mpi_password]}"
	)
end

template "/home/cluster/mpd.hosts" do
	source "mpd.hosts.erb"
	mode 0744
	owner "cluster"
	group "admin"
end
