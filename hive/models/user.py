from typing import Any, Dict

from hive import db
from werkzeug.security import check_password_hash, generate_password_hash

from .mixins import UserTimeMixin, now


class User(UserTimeMixin, db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password = db.Column(db.String(256))
    api_key = db.Column(db.String(256), index=True, unique=True, nullable=True)
    enabled = db.Column(db.Boolean(), nullable=False, default=True)

    organizations = db.relationship("Organization", secondary="orgs_users", back_populates="users")

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}-{}>'.format(self.username, self.id)

    def is_authenticated(self):
        if self.id is not None:
            return True
        else:
            return False

    def is_active(self):
        return self.enabled

    def is_anonymous(self):
        if self.id is None:
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def verify_password(self, pwd: Any):
        return check_password_hash(self.password, pwd)

    def update_profile(self, form: Dict) -> (str, bool):
        new_password = form.get("new_password")
        if new_password:  # are we updating our password?
            new_password_2 = form.get("verify_new_password")
            if new_password_2 is None:
                return "Confirm new password.", False
            else:
                if new_password != new_password_2:
                    return "New passwords must match.", False
                else:
                    self.password = generate_password_hash(new_password)
                    self.save()
        new_email = form.get("new_email")
        if not User.query.filter_by(email=new_email).exists():
            self.email = new_email
            self.save()
        else:
            return "Email already in use.", False
        return None, True

    def refresh(self):
        self.last_seen = now()
        self.save()
