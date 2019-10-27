from flask import Flask, g
from flask.sessions import SecureCookieSessionInterface
from flask_login import LoginManager, user_loaded_from_header
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
import os
import logging

logger = logging.getLogger("hive")

logger.info("Begin Initialization")

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

DB_URI = os.getenv("DATABASE_URI") or 'sqlite:///app.db'
SECRET_KEY = os.getenv("SECRET_KEY") or \
             '7640da40298286a6e462d5a80f1c608b0df8660fb13bd5aad0f32b6db68b42c0'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.secret_key = SECRET_KEY
login_manager = LoginManager(app)


class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)


app.session_interface = CustomSessionInterface()


@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True


db = SQLAlchemy(app)

logger.info("End Initialization")
logger.info("Begin Database Wiring")

import models  # noqa: F401
migrate = Migrate(app, db)

with app.app_context():
    upgrade(directory='migrations', sql=False)
logger.info("End Database Wiring")


from controllers import app as home_controller
app.register_blueprint(home_controller)

if __name__ == "__main__":
    app.run(port=8080, use_reloader=False)
