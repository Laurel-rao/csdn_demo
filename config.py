#！/usr/bin/env python 
# -*- coding:utf-8  -*-

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# database


host = "localhost"
port = 3306
username = "root"
password = "root"
database = "myflask"


class Config(object):

    #格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.\
        format(username, password, host, port, database)
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



