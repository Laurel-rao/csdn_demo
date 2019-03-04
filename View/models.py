#！/usr/bin/env python 
# -*- coding:utf-8  -*-
from datetime import datetime

from View import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return '<用户名:{}>'.format(self.username)
