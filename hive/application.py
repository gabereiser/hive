from flask import Flask
from flask_login import LoginManager
from hashlib import sha256
from logging import basicConfig, getLogger, INFO
from hive import db, migrate
from hive.models import User
from .config import Config
from .controllers import auth_controller, docker_controller, service_controller, user_controller


basicConfig(level=INFO)

log = getLogger(__name__)


class Application(Flask):
    _login_manager: LoginManager

    def __init__(self, test_config=None):
        """
        Initialize Application
        Args:
            test_config: Optional config dict to initialize with instead of .config.py
        """
        super().__init__(__name__, static_url_path='',
                         static_folder='static',
                         template_folder='templates')

        if test_config is None:
            # load the instance config, if it exists, when not testing
            self.config.from_object(Config)
        else:
            # load the test config if passed in
            self.config.from_mapping(test_config)

        self.init()

    def init(self):
        with self.app_context():  # initialize bindings, database, routes
            db.init_app(self)
            migrate.init_app(self, db)

            self._route_bind()
            self._auth_setup(LoginManager(self))
            self._bootstrap()

    def _auth_setup(self, login_manager):
        login_manager.login_view = "/login"

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        self._login_manager = login_manager

    @staticmethod
    def _bootstrap():
        #try:
        admin = User.query.get(1)
        if admin is None:
            log.info("Creating initial admin user...")
            admin = User("admin", "support@testsquad.io")
            admin.password_hash = sha256("admin".encode('utf8')).hexdigest()
            db.session.add(admin)
            db.session.commit()
            log.info("Done, login with admin/admin")
        #except:
        #    pass

    def _route_bind(self):
        self.register_blueprint(auth_controller.route)
        self.register_blueprint(docker_controller.route)
        self.register_blueprint(service_controller.route)
        self.register_blueprint(user_controller.route)
