# Installs a Nginx server with custome HTTP header

exec {'update':
  command  => 'sudo apt-get -y update',
}

exec {'install Nginx':
  command  => 'sudo apt-get -y install nginx',
}

exec { 'add_header':
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

exec { 'restart Nginx':
  command  => 'sudo service nginx restart',
}
