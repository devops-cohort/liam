from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import shen_user
from flask_login import LoginManager, current_user
from application import login_manager

class RegistrationForm(FlaskForm):

    username = StringField('Username',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Enter')
class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateForm(FlaskForm):
    shen_name = StringField('Shen Name',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    power_rating = IntegerField('Power Rating',
        validators=[
            DataRequired(),
            Length(min=1, max=1)
        ]
    )

    description = StringField('Description',
        validators=[
            DataRequired(),
            Length(min=2, max=500)
        ]
    )

class AccountForm(FlaskForm):
    username = StringField('Username',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = shen_user.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already taken. Please choose another.')

