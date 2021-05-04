from hive.models import User
from test import app


class TestCaseMixin:

    @staticmethod
    def client():
        return app.test_client()

    @staticmethod
    def get_admin_user():
        return User.query.first()
