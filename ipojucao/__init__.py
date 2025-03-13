from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy.ext.mypy.util import info_for_cls
import os
import sqlalchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '6d07bfc6805eaa3a624d6d99429b25ef'
if os.getenv("DATABASE_PUBLIC_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_PUBLIC_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipojucao2.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from ipojucao import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        # database.drop_all()
        database.create_all()
        print("Base de dados Criado")
else:
    ("Base de dados já existente")






from ipojucao import routes
