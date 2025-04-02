# 0-the_sky_is_the_limit_not.pp

file { '/etc/security/limits.conf':
    ensure  => present,
    content => 'nginx soft nofile 10000
                nginx hard nofile 10000',
}

service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/security/limits.conf'],
}
