#！/usr/bin/env python 
# -*- coding:utf-8  -*-
from flask import Blueprint

from .views import get_name

urlAPI = Blueprint("urls", __name__)

@urlAPI.route("/hello/", methods=["GET"])
def hello_world():
    # user = User.query.get(0).username
    name = get_name()
    return name


