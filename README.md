# Описание

API к проекту Yatube.
Yatube — это платформа для блогов.
Блог-сервис даёт возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

Документация http://127.0.0.1:8000/redoc/

## Установка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/agvostrikova/api_final_yatube

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS
    ```
    source env/bin/activate
  ```
* Если у вас windows

    ```
    source env/scripts/activate
    ```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## Примеры
