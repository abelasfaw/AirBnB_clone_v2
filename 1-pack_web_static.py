#!/usr/bin/python3
#generates a .tgz archive from the contents of the web_static folder



from fabric.api import *
from os.path import exists
from os import mkdir
from datetime import datetime


def do_pack():
    """generate a .tgz archive"""
    t = datetime.now()
    y,m,d,h,m,s = t.year,t.month,t.day,t.hour,t.minute,t.second
    output_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(y,m,d,h,m,s)
    if (not exists('versions')):
    	mkdir('versions')
    local("tar -zcvf {} web_static".format(output_file))
