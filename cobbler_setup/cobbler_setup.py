#! /usr/bin/python
# -*- coding:utf-8  -*-

import click
import argparse
import os
from threading import Thread

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--distro",dest='distro', help="distro's path, iso image path")
parser.add_argument("--distro_name",dest='distro_name', help="distro's name", required=True)
parser.add_argument("--profile_name",dest='profile_name', help="profile's name", required=True)
parser.add_argument("--mac",dest='mac', default=None, help="mac's address")
parser.add_argument("--system_name",dest='system_name', default=None, help="system's name")
parser.add_argument("--timeout",dest='timeout', default=None, help="timeout automatic choose profile")
parser.add_argument("--ks",dest='ks', required=True, help="the kickstart's path, it must under /var/lib/cobbler/kickstarts/ ")



def execute_cmd(cmd):
    print(cmd)

    if isinstance(cmd, list):
        for i in cmd:
            os.system(i)
    else:
        return os.system(cmd)

def execute_cmd_sync(cmd):
    """

    :param cmd: type list
    :return:
    """
    print(cmd)

    threads = []
    if isinstance(cmd, list):
        for i in cmd:
            thread = Thread(target=execute_cmd, args=(i,))
            threads.append(thread)
        for i in threads:
            i.setDaemon(False)
            i.start()
    else:
        return os.system(cmd)

def retrieve_cmd(cmd):
    print(cmd)
    return os.popen(cmd).read()

def import_distro(distro, distro_name):
    cmd = ['cobbler import --path=%s --name=%s'%(distro, distro_name), 'cobbler distro list']
    for i in cmd:
        print(retrieve_cmd(i))


def create_profile(profile_name, ks, distro_name):
    cmd = ['cobbler profile add --name=%s --kickstart=%s --distro=%s'%(profile_name, ks, distro_name), 'cobbler profile list']
    for i in cmd:
        print(retrieve_cmd(i))

def set_default_profile(profile_name, timeout=None):
    if not is_profile(profile_name):
        return
    edit_cmd = ["sed -i 's/^ONTIMEOUT.*/ONTIMEOUT %s/' /var/lib/tftpboot/pxelinux.cfg/default"%profile_name]
    if timeout is not None and isinstance(timeout, int):
        edit_cmd += "sed -i 's/^TIMEOUT.*/TIMEOUT %s/' /var/lib/tftpboot/pxelinux.cfg/default" % timeout
    execute_cmd(edit_cmd)

def is_profile(profile_name):
    cmd = "cobbler profile list | grep '^   %s$'"%profile_name
    result = retrieve_cmd(cmd)
    if not result:
        print("Error, the profile_name isn't exist")
        return False
    return True

def create_system(mac, system_name, profile_name):
    cmd = ['cobbler system add --mac=%s --name=%s --profile=%s --interface=eth0'%(mac, system_name, profile_name), "cobbler system list"]
    if not (mac and system_name, profile_name):
        print("mac system_name must be set")
        return

    if not is_profile(profile_name):
        return

    for i in cmd:
        print(retrieve_cmd(i))


args = parser.parse_args()

def main(distro, profile_name, ks, distro_name, mac, system_name, timeout):
    # import_distro(distro, distro_name)
    create_profile(profile_name, ks, distro_name)
    create_system(mac, system_name, profile_name)
    # set_default_profile(profile_name, timeout)

if __name__ == '__main__':
    main(args.distro, args.profile_name, args.ks, args.distro_name, args.mac, args.system_name, args.timeout)
