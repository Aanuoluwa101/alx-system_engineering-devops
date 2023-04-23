# modify client-side config file
include stdlib

file_line {
    'password_authentication':
        ensure => present,
        path   => '~/.ssh/config',
        line   => '    PasswordAuthentication no'
    ;
    'file_location':
        ensure => present,
        path   => '~/.ssh/config',
        line   => '    IdentityFile ~/.ssh/school'
}
