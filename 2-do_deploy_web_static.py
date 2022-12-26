#!/usr/bin/python3
# script that distributes an archive to two web servers.
from fabric.api import *
from os.path import exists
from os import mkdir
from datetime import datetime


env.hosts = ['54.167.86.129', '18.234.80.6']
env.user = 'ubuntu'


def do_pack():
    """generate a .tgz archive"""
    t = datetime.now()
    y, m, d, h, m, s = t.year, t.month, t.day, t.hour, t.minute, t.second
    output_file = "versions/web_static_{}{}{}{}{}{}.tgz".\
        format(y, m, d, h, m, s)
    if (not exists('versions')):
        mkdir('versions')
    local("tar -zcvf {} web_static".format(output_file))


def do_deploy(archive_path):
    """distributes an archive to servers in env.hosts"""
    if (not exists(archive_path)):
        return False
    remote_archive_path = "/tmp/{}".format(archive_path.split("/")[-1])
    print("remote archive path: {}".format(remote_archive_path))
    result = put(archive_path, remote_archive_path)
    if result.failed:
        return False
    uncompressed_folder = "/data/web_static/releases/{}".\
    format(archive_path.split("/")[-1].split(".")[0])
    print("uncompressed folder: {}".format(uncompressed_folder))
    result = run("mkdir -p {}".format(uncompressed_folder))
    if result.failed:
        return False
    result = run("tar -zxvf {} -C {}".\
                 format(remote_archive_path, uncompressed_folder))
    if result.failed:
        return False
    result = sudo("rm -f {}".format(remote_archive_path))
    if result.failed:
        return False
    uncompressed_files = "{}/web_static/*".format(uncompressed_folder)
    print("uncompressed files: {}".format(uncompressed_files))
    result = sudo("mv {} {}".format(uncompressed_files, uncompressed_folder))
    if result.failed:
        return False
    web_static_folder = "{}/web_static".format(uncompressed_folder)
    print("Web static folder: {}".format(web_static_folder))
    result = sudo("rm -rf {}".format(web_static_folder))
    if result.failed:
        return False
    result = sudo("rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = sudo("ln -s {} /data/web_static/current".\
                  format(uncompressed_folder))
    if result.failed:
        return False
    return True
