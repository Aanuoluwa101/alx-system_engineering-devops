file { '~/.ssh/config':
    ensure  => 'present',
    content => '
      Host my_server
          HostName 35.175.126.170 
          IdentityFile ~/.ssh/school
          PasswordAuthentication no 
    ',
    mode    => '0600'
}
