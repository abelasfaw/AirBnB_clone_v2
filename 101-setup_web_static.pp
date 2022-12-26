# static deployment config using puppet

exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'install':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'dir-1':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'dir-2':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'page-content':
  command => '/usr/bin/env echo "Holberton School" > /data/web_static/releases/test/index.html',
}
-> exec {'link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'config':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart':
  command => '/usr/bin/env service nginx restart',
}
-> exec {'owner':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
