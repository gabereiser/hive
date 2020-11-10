from hive import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    api_key = db.Column(db.String(256), index=True, unique=True, nullable=True)
    privilege = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def is_authenticated(self):
        if self.id is not None:
            return True
        else:
            return False

    def is_active(self):
        return True

    def is_anonymous(self):
        if self.id is None:
            return True
        else:
            return False

    def is_admin(self):
        if self.privilege == 255:
            return True
        return False

    def get_id(self):
        return self.id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
