#! /usr/bin/python
# -*- coding:utf-8  -*-
import traceback

import requests

from zabbix_api.logs import logger


def get_requests_data(url):
    try:
        beauty = requests.get(url)
    except Exception as e:
        logger.error("访问失败 %s"%e)
        traceback.print_exc()
    else:
        logger.info("访问成功")
        return beauty.content

def write_to_file(filename, data):
    """
        save picture to file
    :param filename:
    :param data:
    :return:
    """
    with open(filename, "wb") as ff:
        ff.write(data)

def main():
    url = 'http://i1.zhiaigou.com/uploads/tu/201909/10350/b65e43822d_33.jpg'
    data = get_requests_data(url)
    if data is None:
        logger.error("访问失败，程序退出")
    else:
        filename = "beauty.jpg"
        write_to_file(filename, data)
        logger.info("写入成功，程序结束")


if __name__ == '__main__':
    main()