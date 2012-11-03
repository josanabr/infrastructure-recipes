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
  password "$1$s31ueI5g$Az.xOP4j.m74bXXrOiFqN."
  support :manage_home => true
end

execute "ssh-keygen" do
  user "hduser"
  group "hadoop"
  cwd "/home/hduser"
  command "ssh-keygen -t rsa -N \"\" -f ~/.ssh/id_rsa"
  action :run
end

execute "authorized hosts" do
  user "hduser"
  group "hadoop"
  cwd "/home/hduser"
  command "cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys"
  action :run
end
