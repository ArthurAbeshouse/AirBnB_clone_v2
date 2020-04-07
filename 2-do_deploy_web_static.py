#!/usr/bin/python3
"""Fabric script that distributes an archive to the web servers"""

from datetime import datetime
from fabric.api import *
import os
env.hosts = ['35.243.212.54', '3.88.185.245']


def do_pack():
    """Generates a .tgz archive"""
    File = datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        if os.path.exists("versions/") is False:
            os.mkdir("versions/")
        local("tar -cvzf versions/web_static_{} web_static".format(File))
        return File
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[1]
        if file_name[-4:] == ".tgz":
            split_path = file_name[:-4]
        new_dirctory = "/data/web_static/releases/" + split_path
        run("sudo mkdir -p " + new_dirctory)
        run("sudo tar -xzf /tmp/" + file_name + " -C " + new_dirctory)
        run("sudo rm /tmp/" + file_name)
        run("sudo mv " + new_dirctory + "/web_static/* " + new_dirctory)
        run("sudo rm -rf " + new_dirctory + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + new_dirctory + " /data/web_static/current")
        return True
    except:
        return False
