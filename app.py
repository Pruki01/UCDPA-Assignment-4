import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, flash, url_for
import psycopg2
from sqlalchemy import create_engine, text
from cinema.forms import LoginForm

config = load_dotenv()
DB = os.environ['DB']
DATABASE = os.environ['DATABASE']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']

engine = create_engine(f'{DB}://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}')
print(engine)
connection = engine.connect()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        for row in result:
            print(f'{row.email} {row.password}')
    connection.close()

    return render_template('index.html', title='Star Movies!')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for email {form.email}, remember_me={form.remember_me}')
        redirect(url_for('index'))
    return render_template('auth/login.html', title='Log In', form=form)