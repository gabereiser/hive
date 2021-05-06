from logging import getLogger

from wsgi import app

config = {
    'ENV': 'test',
    'TESTING': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    'SECRET_KEY': 'supersecret'
}

log = getLogger("tests")


def setup():
    log.info("Initializing Application")
    with app.app_context():
        log.info("Seeding In-Memory Test Database")
        app.seed()


def teardown():
    log.info("Tearing down Application")
    pass
