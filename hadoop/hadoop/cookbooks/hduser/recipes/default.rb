#
# Cookbook Name:: hduser
# Recipe:: default
#
# Copyright 2012, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
group "hadoop" do
end

user "hduser" do
  comment "Hadoop user"
  home "/home/hduser"
  gid "hadoop"
  shell "/bin/bash"
  password "$1$A4KSnDeQ$hsCgIThhKTKXgPPO2Ixr6."
  supports :manage_home => true
end

execute "ssh-keygen" do
  user "hduser"
  group "hadoop"
  cwd "/home/hduser"
  command "ssh-keygen -t rsa -N \"\" -f /home/hduser/.ssh/id_rsa"
  action :run
end

execute "authorized hosts" do
  user "hduser"
  group "hadoop"
  cwd "/home/hduser"
  command "cat /home/hduser/.ssh/id_rsa.pub >> /home/hduser/.ssh/authorized_keys"
  action :run
end
