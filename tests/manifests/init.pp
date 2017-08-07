# The PuppetLabs module invokes Puppet itself to restart the
# RabbitMQ service when setting the erlang_cookie -- but it sets the
# PATH environment variable manually, and it doesn't include the *real*
# location of puppet in this machine.  The simplest is to symlink it
# to /usr/local/bin, which *is* in PATH.
file { '/usr/local/bin/puppet':
  ensure => "link",
  target => "/opt/vagrant_ruby/bin/puppet",
}

host { 'rabbit.ehimeprefecture.com':
  ip           => "192.168.50.100",
  host_aliases => "rabbit",
}

package { "python-pika":
  ensure => installed,
}
