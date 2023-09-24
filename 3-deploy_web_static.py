#!/usr/bin/python3
"""
This script distributes an archive to web servers, using the function
do_deploy
"""
import os
from fabric.api import run, env, cd, put

env.hosts = ['100.25.30.179', '54.87.238.34']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_pack():
    """This function generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone v2, using the function do_pack.
    """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} ./web_static".format(file_name))
        return file_name
    except Exception:
        return None

def do_deploy(archive_path):
    """This function distributes an archive to web servers"""
    if (os.path.exists(archive_path) is False):
        return False
    filename = '/data/web_static/releases/{}'.format(
        archive_path.strip(".tgz"))
    archive = archive_path.lstrip('versions/')
    run('mkdir -p {}'.format(filename))
    # run('mkdir /tmp/versions')
    put('{}'.format(archive_path), "/tmp/")
    run('tar -xzf /tmp/{} -C {}'.format(archive, filename))
    run('mv {}/web_static/* {}'.format(filename, filename))
    run('rm -rf {}/web_static/'.format(filename))
    run('rm /tmp/{}'.format(archive))
    run('rm /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(filename))
    return True