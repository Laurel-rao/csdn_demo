from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from View.urls import urlAPI
from config import Config


app = Flask(__name__)
# app.config.from_mapping({"DEBUG":True})
app.config["DEBUG"] = True
# url 路由转发， blueprint相当于处理的视图

app.register_blueprint(urlAPI, url_prefix="/all")
app.config.from_object(Config)
# 建立数据库关系
db = SQLAlchemy(app)
# 绑定app和数据库，以便进行操作
migrate = Migrate(app, db)

from View import models


if __name__ == '__main__':
    app.run()
