import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# init SQLAlchemy so we can use it later in our models
app.config['SECRET_KEY'] = 'ed450d8caed78e28622ffb0cb9e613fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from app import routes
