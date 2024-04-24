# Puppet manifest to ensure SSH client configuration

$config = "IdentityFile ~/.ssh/school
PubKeyAuthentication yes
PasswordAuthentication no
"

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => $config,
}