from hive.application import Application
from hive.database import db

config = {
    'ENV': 'test',
    'TESTING': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    'SECRET_KEY': 'supersecret'
}


class TestCaseMixin:

    @staticmethod
    def create_app():
        app = Application(test_config=config)
        app.init(testing=True)
        with app.app_context():
            app.seed()
        return app