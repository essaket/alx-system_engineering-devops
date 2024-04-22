# Nginx

#update the server and install nginx
exec {'update & nginx':
  command => 'sudo apt -y update; sudo apt install -y nginx',
  path    => ['/usr/bin', '/usr/sbin/']
}

# create index.html
file {'/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  owner   => 'ubuntu',
  content => "Hello World!\n",
}

# create 404.html
file {'/var/www/html/404.html':
  ensure  => 'file',
  path    => '/var/www/html/404.html',
  owner   => 'ubuntu',
  content => "Ceci n'est pas une page\n",
}

# create or modify default config
file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  owner   => 'ubuntu',
  content => "server {
   listen 80 default_server;
   listen [::]:80 default_server;

   root /var/www/html;
   index index.html;
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}"
}

# create symbolic link to availablle config
exec {'symbolic link':
  command => 'sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
  require => File['/etc/nginx/sites-available/default'],
  path    => '/usr/bin',
  onlyif  => 'test ! -f /etc/nginx/sites-enabled/default',
}

# restart nginx service
exec {'ngnix restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', 'bin'],
}
