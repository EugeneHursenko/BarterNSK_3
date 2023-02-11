import click
from app import app
from rich import print


@app.cli.command('tech', short_help='Для технических целей.')
def cli_tech():
    for key, value in app.config.items():
        print(key, '=>', value)
    print(app.config)


@app.cli.command('user-create', short_help='Создание пользователя.')
@click.option('--name', prompt='Имя пользователя (логин)', help='Для входа в систему..', required=True)
@click.option('--password', prompt='Пароль', required=True)
def cli_user_create(name, password):
    print(name)
    print(password)


@app.cli.command('user-list', short_help='Список всех пользователей.')
def cli_user_list():
    print('--------')


@app.cli.command('user-enable', short_help='Включить пользователя.')
@click.option('--name', prompt='Имя пользователя', required=True)
def cli_user_enable():
    print('@todo')


@app.cli.command('user-disable', short_help='Отключить пользователя.')
@click.option('--name', prompt='Имя пользователя', required=True)
def cli_user_disable():
    print('@todo')


@app.cli.command('user-change-password', short_help='Поменять пароль пользователю.')
@click.option('--name', prompt='Имя пользователя (логин)', help='Для входа в систему.', required=True)
@click.option('--password', prompt='Новый пароль', required=True)
def cli_user_change_password():
    print('@todo')

