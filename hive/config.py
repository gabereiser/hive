import os

basedir = os.getcwd()
print("BASEDIR {}".format(basedir))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = os.getenv("SECRET_KEY") or \
        '0000000000000000000000000000000000000000000000000000000000000000'
    REMEMBER_COOKIE_DURATION = 15 * 60  # in seconds...  15 minutes
