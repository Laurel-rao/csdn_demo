from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)

api = Blueprint("api", __name__)
Config.ini_app(app)
db = SQLAlchemy(app)

from .views import Information

resource = Api(api)
resource.add_resource(Information, "/")

app.register_blueprint(api)