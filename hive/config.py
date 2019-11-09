import os

basedir = os.getcwd()
print("BASEDIR {}".format(basedir))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = os.getenv("SECRET_KEY") or \
        '7640da40298286a6e462d5a80f1c608b0df8660fb13bd5aad0f32b6db68b42c0'
