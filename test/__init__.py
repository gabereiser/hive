from logging import getLogger

from hive.application import Application

config = {
    'ENV': 'test',
    'TESTING': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    'SECRET_KEY': 'supersecret'
}

app = Application(test_config=config)
log = getLogger("tests")


def setup():
    log.info("Initializing Application")
    app.init(testing=True)
    with app.app_context():
        log.info("Seeding In-Memory Test Database")
        app.seed()


def teardown():
    log.info("Tearing down Application")
    pass
