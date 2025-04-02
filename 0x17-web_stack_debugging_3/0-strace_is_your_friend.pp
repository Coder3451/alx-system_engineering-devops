# 0-strace_is_your_friend.pp

file { '/var/www/html':
    ensure => 'directory',
    owner  => 'www-data',
    group  => 'www-data',
    mode   => '0755',
}

file { '/var/www/html/index.html':
    ensure => 'file',
    owner  => 'www-data',
    group  => 'www-data',
    mode   => '0644',
}

service { 'apache2':
    ensure  => 'running',
    enable  => true,
    require => File['/var/www/html'],
}
