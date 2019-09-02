# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end

cookbook_file "gunicorn.service" do
  path "/etc/systemd/system/gunicorn.service"
end

execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end

package "nginx"
cookbook_file "nginx-default" do
  path "/etc/nginx/sites-available/default"
end

execute 'nginx_restart' do
  command 'service nginx restart'
end


# remote_directory '/home/vagrant/mysite' do
#   owner 'vagrant'                                                                 
#   group 'vagrant'
#   mode '0755'
#   source 'mysite'
#   action :create
#   recursive true
# end

package "python3"
package "python3-pip"

execute 'install' do
  command 'pip3 install Django gunicorn psycopg2-binary'
end


execute 'install-2' do
  command 'pip3 install django-tinymce4-lite'
end

package 'python-psycopg2'
package "postgresql"
execute 'postgres_setup' do
  command 'echo "CREATE DATABASE mydb; CREATE USER vagrant; GRANT ALL PRIVILEGES ON DATABASE mydb TO vagrant;" | sudo -u postgres psql'
end

execute 'deploy' do
  command 'sudo service gunicorn restart'
end

execute 'build_sfuanime_model' do
  cwd '/home/vagrant/files/mysite'
  user 'vagrant'
  command 'python3 manage.py makemigrations sfuanime'
end


execute 'build_sfuanime_model2' do
  cwd '/home/vagrant/files/mysite'
  user 'vagrant'
  command 'python3 manage.py sqlmigrate sfuanime 0001'
end



execute 'runserver' do
  cwd '/home/vagrant/files/mysite'
  user 'vagrant'
  command 'python3 manage.py migrate'
end



execute 'load_trade_data' do
  cwd '/home/vagrant/files/mysite'
  user 'vagrant'
  command 'python3 manage.py loaddata sfuanime_sample.json'
end


