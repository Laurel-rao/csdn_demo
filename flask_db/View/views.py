from flask import jsonify

from .models import User
from View import db, app


@app.route("/just", methods=["GET"])
def create_name():
    b = User(username="zhangq", email="hah1a@.com", password_hash="jijizhaha")
    db.session.add(b)
    db.session.commit()
    return jsonify("yes")

@app.route("/get", methods=["GET"])
def get_name():
    user = User.query.filter_by(id=1).values("id", "email")
    for i in user:
        print(i)
    return "users"

@app.route("/", methods=["GET"])
def get1_name():
    return "Hello world"