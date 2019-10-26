from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from controllers import home
import os

app = Flask(__name__, static_url_path='',
               static_folder='static',
               template_folder='templates')

DB_URI = os.getenv("DATABASE_URI") or 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.register_blueprint(home.home_blueprint)

if __name__ == "__main__":
    app.run(port=8080)
