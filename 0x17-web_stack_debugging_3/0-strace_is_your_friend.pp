# 0-strace_is_your_friend.pp

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Ensure the required Apache module is enabled
apache::module { 'cgi':
  ensure => 'present',
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Package['apache2'],
}
