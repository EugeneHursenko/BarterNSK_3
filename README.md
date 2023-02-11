Установка
=========

Установит все зависимости из requirements.txt

```shell
# windows
./install.cmd
```

В скрипте установки есть команда применения миграций БД, по этому сразу после инсталла, БД будет в актуальном состоянии, не зависимо от того проет пустой и только что создался или БД уже существует и нужен внести изменения в структуру - они применятся автоматически.

Запуск на локальной машине для разработки

```shell
# windows
./run.cmd
```

Работа с консольными командами
==============================

Работает только из под PyCharm, в ином случае, нужно зайти в venv.

Получения списка всех доступных команд
```shell
flask
```

Создание нового пользователя
```shell
flask user-create
```

Работа с миграциями БД

```shell
# Создание скрипта миграции
flask db revision 'Комментарий к изменению схемы БД'

# Применение новых миграций
flask db upgrade
```

