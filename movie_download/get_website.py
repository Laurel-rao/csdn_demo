#! /usr/bin/python
# -*- coding:utf-8  -*-
import re
import traceback

from bs4 import BeautifulSoup
import requests


def get_content():
    with open("./re.txt", encoding="utf-8") as fff:
        data = fff.read()
    return data

def get_url():
    data = get_content()
    bea_data = BeautifulSoup(data, "html")
    a_tags = bea_data.find_all("a")
    urls = [tag.get("href") for tag in a_tags]
    return urls

def main():
    urls = get_url()
    for i in urls:
        name = re.split("/", i)[-1]
        i = "https://cisco.lab.spoto.cloud/manual/" + i[1:]
        print("url == %s"%i)
        data = reqeust_website(i)
        write_to_file(name, data)

def write_to_file(name, content):
    with open("./html/" + name, "wb") as ff:
        ff.write(content)

def reqeust_website(url=None):
    try:
        req = requests.get(url)
    except:
        traceback.print_exc()
        return ""
    else:
        return req.content




# https://cisco.lab.spoto.cloud/manual/Solution/01-Manage_IOS.html

if __name__ == '__main__':
    main()
