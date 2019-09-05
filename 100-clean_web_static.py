#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, put, run
from datetime import datetime
from os.path import exists


env.hosts = ['35.196.4.24', '35.190.128.47']


def do_pack():
    """
    Pack webstatic dir into a .tgz archive
    """
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(current_time)
    tgz_file = local("tar -cvzf {} web_static".format(name))
    return tgz_file


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            tgz_file = archive_path.split("/")[1].split(".")[0]
            remote_path = "/data/web_static/releases/{}".format(tgz_file)
            run("mkdir {}".format(remote_path))
            run("tar -zxvf /tmp/{}.tgz --directory {}/".format(
                tgz_file, remote_path))
            run("rm /tmp/{}".format(archive_path.split("/")[1]))
            run("rm /data/web_static/current")
            run("ln -sf /data/web_static/releases/{}\
             /data/web_static/current".format(tgz_file))
            run("mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/current/".format(tgz_file))
            run("rm -rf /data/web_static/releases/{}/web_static/"
                .format(tgz_file))
            return True
    return False
