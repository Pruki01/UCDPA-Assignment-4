from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from cinema.models import User

class LoginForm(FlaskForm):
    email       = EmailField('Email', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email       = EmailField('Email', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    confirm_p   = PasswordField('Confirm Password', validators=[DataRequired()])
    submit      = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email is already registered. Please use another!')

    def validate_password(self, password, confirm_p):
        pass