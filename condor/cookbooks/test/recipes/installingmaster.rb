include_recipe "test::settingupfiles"

execute "install" do
	user "root"
	group "admin"
	cwd "/tmp/condor"
	command "bash install.bash -t ms -p /opt -u condor -d cluster.org,10.0.2.15 -b -s"
	action :run
end
