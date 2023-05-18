#!/usr/bin/env python3
from fabric.api import *

env.hosts = ['54.90.50.38']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def install_mysql():
    put('signature.key', '~/')
    put('install_mysql', '~/')
    run('chmod u+x ~/install_mysql')
    run('cd ~/')
    run('./install_mysql')
