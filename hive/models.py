from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    priv = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def is_authenticated(self):
        if self.id > 0:
            return True
        else:
            return False

    def is_active(self):
        return self.active

    def is_anonymous(self):
        if self.id is None:
            return True
        else:
            return False

    def get_id(self):
        return self.id
