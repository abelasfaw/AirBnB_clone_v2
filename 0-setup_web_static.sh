#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

#install nginx
apt-get -y update
apt-get -y install nginx
#allow Nginx
ufw allow 'Nginx HTTP'
#create project folders
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
#create a test page
test_page="<html>
   <head>
   </head>
   <body>
      Holberton School
   </body>
</html>"
echo "$test_page" > /data/web_static/releases/test/index.html
#create a symbolic link 
ln -sf /data/web_static/releases/test /data/web_static/current
#Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data
#Update the Nginx configuration to serve the content of
#/data/web_static/current/ to hbnb_static
sudo sed -i "/server_name _;/c\ \tserver_name _;\n\tlocation /hbnb_static {\n\t  alias /data/web_static/current/;\n\t  autoindex off;\n\t}" /etc/nginx/sites-available/default
#restart nginx
service nginx restart
exit
