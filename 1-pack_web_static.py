#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


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
