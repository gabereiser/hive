from flask_mail import Mail
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
manager = Manager()
