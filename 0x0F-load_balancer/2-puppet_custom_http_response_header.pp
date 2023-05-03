# Configures a custom response header

exec { 'update':
  command  => 'sudo /usr/bin/apt-get update',
  provider => shell,
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
}

file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

exec { 'redirect':
  command  => 'sudo sed -i "/server_name _;/a \        rewrite ^/redirect_me \
                 https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" \
                 /etc/nginx/sites-available/default',
  provider => shell,
  require  => Package['nginx'],
  notify   => Service['nginx']
}

exec {'error_404':
  command  => 'sudo sed -i "/server_name _;/a \        error_page 404 \
                 /custom_404.html;" /etc/nginx/sites-available/default',
  provider => shell,
  require  => [
    Package['nginx'],
    File['/var/www/html/custom_404.html']
  ],
  notify   => Service['nginx']
}

exec {'add_header':
  command  => 'sudo sed -i "/server_name _;/a \        add_header X-Served-By \
                 $(hostname);" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Package['nginx'],
  notify   => Service['nginx']
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => [
    Exec['add_header'],
    File['/var/www/html/index.html'],
    Exec['redirect'],
    Exec['error_404']
  ]
}
