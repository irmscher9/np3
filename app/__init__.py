from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1c42e22df7b4d8bb636c328a2ffcd6fe990402ae125c2a07'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app import routes