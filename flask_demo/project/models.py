from project import db


class Device(db.Model):
    __tablename__ = "Device"

    device_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    name = db.Column(db.String(255), default="")