# Lab 2 Django CRUD

## Что внутри

- `crudproject` — конфигурация Django-проекта
- `crudapp` — приложение с моделью заказов и CRUD-операциями
- `templates/` — шаблоны страниц
- `DOC_ANALYSIS.md` — краткий разбор исходного задания

## Как запустить

После установки Django:

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Доступные страницы:

- `/` — главная страница
- `/orders/` — список заказов
- `/orders/new/` — создание заказа
- `/admin/` — административная панель

## Docker

Сборка и запуск:

```bash
docker compose up --build
```

После старта контейнер:

- применяет миграции;
- пытается создать суперпользователя из переменных окружения;
- запускает сервер на `0.0.0.0:8000`.

Доступ:

- сайт: `http://127.0.0.1:8000/`
- админка: `http://127.0.0.1:8000/admin/`
- логин: `admin`
- пароль: `admin12345`
