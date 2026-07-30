from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from cinema.models import User
from cinema.forms import LoginForm, RegistrationForm
from app import app, session

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

        if user is None or not user.check_password(form.password.data):

            flash('Invalid username or password!')
            return redirect(url_for('login'))


        login_user(user, form.remember_me.data)
        return redirect(url_for('index'))

    else:
        print(form.errors)

    return render_template('auth/login.html', title='Log In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        session.add(new_user)
        session.commit()
        return redirect(url_for('index'))

    else:
        print(form.errors)

    return render_template ('auth/registration.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))