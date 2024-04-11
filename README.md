# Описание

API к проекту Yatube.
Yatube — это платформа для блогов.
Блог-сервис даёт возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

Документация доступна после запуска сервера http://127.0.0.1:8000/redoc/

Спецификация в ОpenAPI находится в директории postman_collection, доступна без запуска сервера. 

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
Обновить pip:
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

## Примеры запросов

POST .../api/v1/posts/
```
{
    "text": "Пост с группой",
    "group": {{group_id}}
}
```
Пример ответа:
```
{
    "id": 17,
    "author": "regular_user",
    "text": "Пост с группой",
    "pub_date": "2024-04-10T18:19:04.870871Z",
    "image": null,
    "group": 1
}
```
POST .../api/v1/posts/{{post_with_group}}/comments/
```
{
    "text": "Тестовый комментарий"
}
```
Пример ответа:
```
{
    "id": 3,
    "author": "regular_user",
    "text": "Тестовый комментарий",
    "created": "2024-04-10T18:20:24.203001Z",
    "post": 17
}
```
GET .../api/v1/groups/{{group_id}}/

Пример ответа:
```
{
    "id": 1,
    "title": "TestGroup",
    "slug": "test-group",
    "description": "Some text."
}
```

