from flask import jsonify

from .models import User
from View import db, app


@app.route("/just", methods=["GET"])
def get_name():
    b = User(username="zhangq", email="hah1a@.com", password_hash="jijizhaha")
    db.session.add(b)
    db.session.commit()
    return jsonify("yes")