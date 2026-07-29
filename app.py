import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cinema.forms import LoginForm
from cinema.models import User
from flask_login import current_user, login_user, logout_user

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

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@app.route('/')
def index():

    return render_template('index.html', title='Star Movies!')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():

        user = session.query(User).filter(User.email == form.email.data).one()

        if user is None or user.check_password(form.password.data):

            flash('Invalid username or password!')
            return redirect(url_for('login'))


        login_user(user, form.remember_me.data)

    return redirect(url_for('index'), title='Log In')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))