#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Pack webstatic dir into a .tgz archive
    """
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(current_time)
    tgz_file = local("tar -cvzf {} web_static".format(name))
    return tgz_file
