# Install flask from pip3

exec { 'install_flask':
  command => '/path/to/your/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/path/to/your/pip3 show Flask | grep Version',
}

