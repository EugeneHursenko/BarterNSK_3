from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
    ValidationError,
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp ,Optional
from .models import User


class CategoryForm(FlaskForm):
    title = StringField(label='Название', validators=[InputRequired()])


class LoginForm(FlaskForm):
    email = StringField(label='Емаил', validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(label='Пароль', validators=[InputRequired(), Length(min=3, max=72)])
    remember_me = BooleanField(label='Запомнить')
    name = StringField(
        validators=[Optional()]
    )


class RegisterForm(FlaskForm):
    name = StringField(
        label='Имя',
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(
        label='Пароль',
        validators=[InputRequired(), Length(4, 72)]
    )
    cpassword = PasswordField(
        label='Повтор пароля',
        validators=[
            InputRequired(),
            Length(4, 72),
            EqualTo('password', message='Пароли должны совпадать'),
        ]
    )

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Емаил уже занят')

    def validate_name(self, name):
        if User.query.filter_by(name=name.data).first():
            raise ValidationError('Имя пользователя уже занято')
