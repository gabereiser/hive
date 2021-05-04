import base64
import uuid

from flask import Flask
from flask.cli import AppGroup
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_script import Manager
from logging import basicConfig, getLogger, INFO

from werkzeug.security import generate_password_hash
from hive.database import db
from hive.models import User
from hive.models import Organization
from .config import Config
from .controllers import auth_controller, docker_controller, service_controller, user_controller


basicConfig(level=INFO)

log = getLogger(__name__)

cli = AppGroup("admin")


class Application(Flask):
    _login_manager: LoginManager
    _manager: Manager
    _mail: Mail
    _migrate: Migrate

    def __init__(self, test_config=None):
        """
        Initialize Application
        Args:
            test_config: Optional config dict to initialize with instead of .config.py
        """
        super().__init__(__name__, static_url_path='',
                         static_folder='static',
                         template_folder='templates')

        self._mail = Mail()
        self._migrate = Migrate()
        self._manager = Manager()

        if test_config is None:
            # load the instance config, if it exists, when not testing
            self.config.from_object(Config)

        else:
            # load the test config if passed in
            self.config.from_mapping(test_config)

    def init(self, testing: bool = False):
        with self.app_context():  # initialize bindings, database, routes
            db.init_app(self)
            self._migrate.init_app(self, db)
            self._mail.init_app(self)
            self._route_bind()
            self._auth_setup(LoginManager(self))
            self.cli.add_command(cli)
            if testing:
                db.drop_all()
                db.create_all()

    def _auth_setup(self, login_manager):
        login_manager.login_view = "/login"

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(user_id)

        @login_manager.request_loader
        def load_user_from_request(request):

            # first, try to login using the api_key url arg
            api_key = request.headers.get('api_key')
            if api_key:
                user = User.query.filter_by(api_key=api_key).first()
                if user:
                    return user

            # next, try to login using Basic Auth
            api_key = request.headers.get('Authorization')
            if api_key:
                header_parts = api_key.split(' ')
                api_key = header_parts[:-1]
                try:
                    api_key = base64.b64decode(api_key)
                except TypeError:
                    pass
                user = User.query.filter_by(api_key=api_key).first()
                if user:
                    return user

            return None
        self._login_manager = login_manager

    @cli.command("seed")
    def _bootstrap(self):
        self.seed()

    def seed(self):
        try:
            count = User.query.count()
            if count == 0:
                log.info("Creating initial Admin tenant...")
                admin_tenant = Organization("Admin")
                db.session.add(admin_tenant)
                db.session.commit()

                log.info("Creating initial admin user...")
                admin = User("admin", "support@testsquad.io")
                admin.password = generate_password_hash("admin")
                db.session.add(admin)
                db.session.commit()
                log.info(admin.id)
                admin_tenant.add_user(admin, 100)
                log.info("Complete, login with admin/admin")
                return
            log.info("Seed Complete.")
        except RuntimeError as ex:
            pass

    def _route_bind(self):
        self.register_blueprint(auth_controller.route)
        self.register_blueprint(docker_controller.route)
        self.register_blueprint(service_controller.route)
        self.register_blueprint(user_controller.route)
