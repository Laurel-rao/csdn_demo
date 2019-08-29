#！/usr/bin/env python 
# -*- coding:utf-8  -*-

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)
# app.config.from_mapping({"DEBUG":True})
app.config["DEBUG"] = True
# url 路由转发， blueprint相当于处理的视图

app.config.from_object(Config)
# 建立数据库关系
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from View.urls import urlAPI
app.register_blueprint(urlAPI)
from .models import *
