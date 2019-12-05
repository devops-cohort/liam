from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'xxxyeetyfjdjfgweff3278idoof'
# app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.169.195/projdb'
# app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://'+getenv('MYSQL_USER')+":"+getenv('MYSQL_PASSWORD')+"@"+getenv('MYSQL_HOST')+"/"+getenv('MYSQL_DB'))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes