import os
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

config = load_dotenv()
DB = os.environ['DB']
DATABASE = os.environ['DATABASE']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']

engine = create_engine(f'{DB}://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
session = Session()

login = LoginManager(app)
login.login_view = 'login'

import cinema.routes