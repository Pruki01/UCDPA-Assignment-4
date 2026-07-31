from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from cinema.models import User, MovieGenre, MovieStatus
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

class AddMovieForm(FlaskForm):
    title       = StringField('Title', validators=[DataRequired()])
    duration    = IntegerField('Duration', validators=[DataRequired()])
    genre       = SelectField("Genres",
                              choices=[(genre.value, genre.name.title()) for genre in MovieGenre],
                              coerce=MovieGenre,
                              validators=[DataRequired()])
    status      = SelectField("Status",
                              choices=[(status.value, status.name.title()) for status in MovieStatus],
                              coerce=MovieStatus,
                              validators=[DataRequired()])
    file        = FileField('File', validators=[FileRequired()])
    submit      = SubmitField('Add Movie')