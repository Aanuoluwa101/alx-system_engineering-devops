# modify client-side config file
include stdlib

file_line {
    'password_authentication':
        ensure => present,
        path   => '/etc/ssh/ssh_config',
        line   => '    PasswordAuthentication no'
    ;
    'file_location':
        ensure => present,
        path   => '/etc/ssh/ssh_config',
        line   => '    IdentityFile ~/.ssh/school'
}
