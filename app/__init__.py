from flask.json.tag import TagTuple
from config import Konfigurasi
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Konfigurasi)
# app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=20) 
# app.config['USE_SESSION_FOR_NEXT'] = True
# app.config['SECRET_KEY'] = 'mysecret!@%#'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
