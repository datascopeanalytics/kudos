import os

from fabric.api import env, task, execute, run
from fabtools.vagrant import vagrant

import utils
import provision
import serve

# shared environment between local machines and remote machines
# (anything that is different gets overwritten in environment-setting
# functions)
env.mysql_root_password = 'tiyp,kudos'
env.django_user = 'kudos'
env.django_password = 'tiyp,kudos'
env.django_db = 'kudos'
env.repository_path = 'git@github.com:datascopeanalytics/kudos.git'
env.ssh_directory = os.path.expanduser(os.path.join('~', '.ssh'))
web_directory = "web"


@task
def dev():
    """define development server"""
    env.provider = "virtualbox"
    env.remote_path = '/vagrant'
    env.web_path = os.path.join(env.remote_path, web_directory)
    env.config_type = 'dev'
    env.use_repository = False
    env.site_name = None
    env.django_site_id = 1

    utils.set_hosts_from_config()
    execute(vagrant, env.hosts[0])


@task
def prod():
    env.provider = "digitalocean"
    env.remote_path = '/srv/www/kudos'
    env.web_path = os.path.join(env.remote_path, web_directory)
    env.config_type = 'production'
    env.branch = 'master'
    env.use_repository = True
    env.site_name = 'kudos.datasco.pe'
    env.django_site_id = 2

    utils.set_env_with_ssh('kudos')
