#！/usr/bin/env python 
# -*- coding:utf-8  -*-

import requests

url = "https://iqiyi.qq-zuidazy.com/20190220/5569_d8e2612b/800k/hls/f1983596ddb{:0>6d}.ts"

def get_content(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3"}
    resp = requests.get(url, headers=headers)
    return resp.content

def write_content(path, content):
    ff = open(path, "ab")
    ff.write(content)

def main():
    i = 0
    path = "./green_book.ts"
    ff = open(path, "ab")
    while True:
        print(i)
        i += 1
        content = get_content(url.format(i))
        ff.write(content)

if __name__ == '__main__':
    main()