# we create a source directory where johntheripper will be uncompressed
directory "/home/cluster/source" do
	owner "cluster"
	group "admin"
	mode "0755"
	action :create
end
# make johntheripper file available to the VM
cookbook_file "/var/tmp/john-1.7.2-bp17-mpi8.tar.gz" do
	source "john-1.7.2-bp17-mpi8.tar.gz"
	mode 0755
	owner "cluster"
	group "admin"
end
# file is untarred
execute "tar" do
	user "cluster"
	group "admin"
	cwd "/home/cluster/source"
	command "tar xfz /var/tmp/john-1.7.2-bp17-mpi8.tar.gz"
	action :run
end
# file is compiled
execute "make" do
	user "cluster"
	group "admin"
	cwd "/home/cluster/source/john-1.7.2-bp17-mpi8/src"
	command "make clean #{node[:system]}"
	action :run
end
# move the binaries to the ${HOME}/bin directory
execute "move" do
	user "cluster"
	group "admin"
	cwd "/home/cluster/source/john-1.7.2-bp17-mpi8/src"
	command "mv ../run/* /home/cluster/bin"
	action :run
end
