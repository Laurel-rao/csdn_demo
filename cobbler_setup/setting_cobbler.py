#! /usr/bin/python

import os
import re
from threading import Thread



"""
    This scripts is for create cobbler app quickly!

"""

Base = "/etc/cobbler/"
dhcp = 'dhcp.template'
conf = "settings"

def execute_cmd(cmd):
    print cmd
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
    print cmd
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
    print cmd
    return os.popen(cmd).read()

def edit_settings():
    ip_info = retrieve_cmd("ifconfig eth0")
    passwd = retrieve_cmd("openssl passwd -1 -salt '123' 'redhat'").strip()
    print passwd
    ip = re.search("inet (\S*)", ip_info).group(1)
    segment = ".".join(ip.split(".")[:-1])
    print(segment)

    cmds = [
        "sed -i 's/^manage_dhcp:.*/manage_dhcp: 1/' %s"%(Base+conf),
        "sed -i 's/^server:.*/server: %s/' %s"%(ip, Base+conf),
        "sed -i 's/^next_server:.*/next_server: %s/' %s"%(ip, Base+conf),
        "sed -i 's/^manage_tftpd:.*/manage_tftpd: 1/' %s"%(Base+conf),
        "sed -i 's/^pxe_just_once:.*/pxe_just_once: 1/' %s"%(Base+conf),
        "sed -i 's/^default_password_crypted: .*/default_password_crypted: \"%s\"/' %s"%(passwd, Base+conf),
        "sed -i 's/yes/no/' /etc/xinetd.d/tftp",
    ]
    dhcp_cmd = [
        "sed -i 's/^subnet [0-9.]*/subnet %s/' %s"%(segment+".0", Base+dhcp),

    ]
    dhcp_add_cmd = [
        "sed -i '/^subnet /a\     option routers %s;' %s"%(segment+".2", Base+dhcp), 
        "sed -i '/^subnet /a\     option domain-name-servers %s;' %s"%(ip, Base+dhcp),
        "sed -i '/^subnet /a\     option subnet-mask %s;' %s"%("255.255.255.0", Base+dhcp), 
        "sed -i '/^subnet /a\     range dynamic-bootp  %s %s;' %s"%(segment+".100", segment+".200" , Base+dhcp),
    ]

    dhcp_edit_cmd = [
        "sed -i 's/option routers.*/option routers %s;/' %s"%(segment+".2", Base+dhcp), 
        "sed -i 's/option domain-name-servers.*/option domain-name-servers %s;/' %s"%(ip, Base+dhcp),
        "sed -i 's/option subnet-mask.*/option subnet-mask %s;/' %s"%("255.255.255.0", Base+dhcp),
        "sed -i 's/range dynamic-bootp.*/range dynamic-bootp  %s %s;/' %s"%(segment+".100", segment+".200" , Base+dhcp),
    ]
    cmds += dhcp_cmd
    search_cmd = [
        "grep -i 'option router' %s"%(Base+dhcp),  
        "grep -i 'option domain-name-servers' %s"%(Base+dhcp),  
        "grep -i 'option subnet-mask' %s"%(Base+dhcp),  
        "grep -i 'range dynamic-bootp' %s"%(Base+dhcp),
    ]
    for x,y,z in zip(search_cmd, dhcp_add_cmd, dhcp_edit_cmd):
        if retrieve_cmd(x):
            execute_cmd(z)
        else:
            execute_cmd(y)

    for i in cmds:
        execute_cmd_sync(i)

def change_ip(ip):
    eth0 = '/etc/sysconfig/network-scripts/ifcfg-eth0'
    cmd = ["sed -i 's/^IPADDR=.*/IPADDR=%s/' %s"%(ip, eth0),
         "systemctl restart network",
    ]
    execute_cmd(cmd)

def restart_service():
    cmd = "systemctl restart "
    cmds = [
        "cobblerd",
        "rsyncd",
        "tftp",
        "httpd"
    ]
    cmd_list = [cmd + i for i in cmds]
    execute_cmd("cobbler sync")
    # execute_cmd(cmd_list)

if __name__ == "__main__":
    change_ip("192.168.146.133")
    edit_settings()
    restart_service()
