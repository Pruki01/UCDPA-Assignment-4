from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from cinema.models import User
from app import session

class LoginForm(FlaskForm):
    email       = EmailField('Email', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email       = EmailField('Email', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    confirm_p   = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match!')])
    submit      = SubmitField('Register')

    def validate_email(self, email):
        user = session.query(User).filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError('The email is already registered. Please use another!')