from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, upgrade
from hashlib import sha256
from logging import basicConfig, getLogger, INFO
from config import Config
from flask_sqlalchemy import SQLAlchemy

basicConfig(level=INFO)

log = getLogger("HIVE")
db = SQLAlchemy()

def create_app(test_config=None):
    log.info("Begin Initialization")

    app = Flask(__name__, static_url_path='',
                static_folder='static',
                template_folder='templates')
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    with app.app_context():
        db.init_app(app)
        from models import User
        from . import controllers
        login_manager = LoginManager(app)
        login_manager.login_view = "/login"

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))
        try:
            admin = load_user(1)
            print(admin)
            if admin is None:
                admin = User()
                admin.id = 1
                admin.username = "admin"
                admin.password_hash = sha256("admin".encode('utf8')).hexdigest()
                db.session.add(admin)
                db.session.commit()
        except:
            pass
        Migrate(app, db)
        app.register_blueprint(controllers.route)
    return app
