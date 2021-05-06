from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# NOTE: This exists only to provide metadata to models prior to binding
# and act as the global db handle
db = SQLAlchemy()
migrate = Migrate()


def seed():
    pass
