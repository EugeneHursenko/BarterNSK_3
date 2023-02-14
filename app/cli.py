import click
from app import app
from datetime import datetime
from rich import print
from texttable import Texttable
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from . import db


@app.cli.command('tech', short_help='Для технических целей.')
def cli_tech():
    for key, value in app.config.items():
        print(key, '=>', value)
    print(app.config)


@app.cli.command('user-create', short_help='Создание пользователя.')
@click.option('--name', prompt='Имя пользователя (логин)', required=True)
@click.option('--email', prompt='Email', help='Для входа в систему..', required=True)
@click.option('--password', prompt='Пароль', required=True)
def cli_user_create(name, password, email):
    user = User.query.filter_by(email=email).first()

    if user:
        print('Ошибка: Емаил уже занят.')
        return

    user = User.query.filter_by(name=name).first()

    if user:
        print('Ошибка: Имя уже занято.')
        return

    new_user = User(
        email=email,
        name=name,
        created_at=datetime.now(),
        password=generate_password_hash(password, method='sha256')
    )

    db.session.add(new_user)
    db.session.commit()

    print('Успешно: Пользователь создан с ИД = ', new_user.id)


@app.cli.command('user-list', short_help='Список всех пользователей.')
def cli_user_list():
    users = User.query.all()

    t = Texttable()
    t.add_row(['ID', 'Email', 'Name', 'Is Enabled',  'Role', 'Created At'])

    for user in users:
        t.add_row([user.id, user.email, user.name, user.is_enabled, user.role, user.created_at])

    print(t.draw())


@app.cli.command('user-enable', short_help='Включить пользователя.')
@click.option('--email', prompt='Email', required=True)
def cli_user_enable(email):
    user = User.query.filter_by(email=email).first()

    if not user:
        print('Ошибка: Пользователя с таким емаил не существует.')
        return

    if user.is_enabled == 1:
        print('Ничего не требуется: Пользователя уже активен.')
        return

    user.is_enabled = 1

    db.session.add(user)
    db.session.commit()

    print('Успешно: Пользователь активирован')


@app.cli.command('user-disable', short_help='Отключить пользователя.')
@click.option('--email', prompt='Email', required=True)
def cli_user_disable(email):
    user = User.query.filter_by(email=email).first()

    if not user:
        print('Ошибка: Пользователя с таким емаил не существует.')
        return

    if user.is_enabled == 0:
        print('Ничего не требуется: Пользователя уже отключен.')
        return

    user.is_enabled = 0

    db.session.add(user)
    db.session.commit()

    print('Успешно: Пользователь отключен')


@app.cli.command('user-change-password', short_help='Поменять пароль пользователю.')
@click.option('--email', prompt='Email', required=True)
def cli_user_change_password(email):
    user = User.query.filter_by(email=email).first()

    if not user:
        print('Ошибка: Пользователя с таким емаил не существует.')
        return

    print('@todo')

