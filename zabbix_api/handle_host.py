#！/usr/bin/env python 
# -*- coding:utf-8  -*-
import json
import time

import requests

URL = "http://99.14.46.33/zabbix/api_jsonrpc.php"

def login_zabbix():
    '''
        retrieve the token, Authentication
    :return:
    '''
    login_data = {
            "jsonrpc":"2.0",
            "method":"user.login",
            "id":1,
            "auth":None,
            "params":{
                "user": "Admin",
                "password": "zabbix"
            }
    }

    resp_login = requests.post(url=URL, json=login_data)
    auth = resp_login.json().get("result")
    return auth

def get_hosts():

    data = {"jsonrpc":"2.0",
            "method":"host.get",
            "id":1,"auth":None,
            "params":{
                "selectGroups": "extend",
                "selectInterfaces": "extend",
                "selectParentTemplates": [
                    "templateids",
                    "name"
                ],
            }
    }

    auth = login_zabbix()
    data.update({"auth": auth})
    resp = requests.post(url=URL, json=data)
    print(json.dumps(resp.json().get("result"), indent=4, separators=(",", ":")))

def get_host_group():
    data = {"jsonrpc":"2.0",
            "method":"hostgroup.get",
            "id":1,"auth":None,
            "params":{
                "output": "extend",
                # "templateids": "extend",
            }}
    auth = login_zabbix()
    data.update({"auth": auth})
    resp = requests.post(url=URL, json=data)
    print(json.dumps(resp.json().get("result"), indent=4, separators=(",", ":")))


def create_zabbix():
    data = {
            "method":"host.create",
            "params":{
                "host": "My LInux s1erver",
                # "visiblename": "lalala",
                "interfaces":[
                    {"type": 1,
                     "main":1,
                     "useip":1,
                     "ip": "192.168.8.1",
                     "dns": "",
                     "port":"10051",
                     }
                ],
                "groups": [
                    {"groupid":"112321"}
                ],
                "templates": [
                    {
                        "templateid": "10001"
                    }
                ],
                "inventory": {
                    "macaddress_a": "01234",
                    "macaddress_b": "56768"
                }
            },
        "id": 1, "auth": "199d2e96ccc8bc7a0d5c8d6065e1a91f", "jsonrpc": "2.0",
            }
    json_data = {
        "method": "host.create",
        "params": {
            "host": "Web Linux server2",
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "192.168.8.1",
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "12"
                }
            ],
            # "templates": [
            #     {
            #         "templateid": "10001"
            #     }
            # ],
            # "inventory": {
            #     "macaddress_a": "01234",
            #     "macaddress_b": "56768"
            # }
        }
    }
    auth = login_zabbix()

    json_base = {
        "jsonrpc": "2.0",
        "auth": auth,
        "id": 1
    }
    data.update({"auth": auth})
    json_data.update(json_base)
    print(data.get("auth"))
    print(json.dumps(data, indent=4))
    resp = requests.post(url=URL, json=data)
    print(json.dumps(json_data, indent=4))


    return resp.json()

def create_hostgroups():
    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.create",
        "params": {
            "name": "Linux server1"
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
    }
    auth = login_zabbix()

    data.update({"auth": auth})
    print(data.get("auth"))
    resp = requests.post(url=URL, json=data)
    print(resp.json())

def get_template():

    data = {"jsonrpc":"2.0",
            "method":"template.get",
            "id":1,"auth":None,
            "params":{
            }
    }

    auth = login_zabbix()
    data.update({"auth": auth})
    resp = requests.post(url=URL, json=data)
    print(json.dumps(resp.json().get("result"), indent=4, separators=(",", ":")))

if __name__ == '__main__':
    get_template()