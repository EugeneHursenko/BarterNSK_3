Инструменты разработки
======================

Зафиксировать все текущие версии пакетов в зависимостях:

```shell
pip freeze > requirements.txt
```

Посмотреть все пакеты требующие обновления:
```shell
pip list --outdated
```

Update All Python Packages On Windows
```shell
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```

Update All Python Packages On Linux
```shell
# pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U  
```
