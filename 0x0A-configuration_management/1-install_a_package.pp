# Install flask from pip3 by using Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
