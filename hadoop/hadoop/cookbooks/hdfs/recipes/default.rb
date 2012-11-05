#
# Cookbook Name:: hdfs
# Recipe:: default
#
# Copyright 2012, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
execute "modify hadoop-env.sh" do
  user "hduser"
  group "hadoop"
  cwd "/usr/local/apps/hadoop/conf"
  command "sed 's/\# export JAVA.*/export JAVA_HOME=\/usr\/local\/apps\/jdk/g' hadoop-env.sh > tmp.txt ; mv tmp.txt hadoop-env.sh"
  action :run
end