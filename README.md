# DJANGO TEMPLATE

Simple django starter template set up with docker ready for development and production.

it includes :
* Django corsheaders
* Django extensions
* Django debug toolbar
* Allauth for user management
* Email confirmation
* Environment for **Development** and dockerized **Production**
* SQLite3 Database (Development)
* Postgresql Database (Production)
* Base html template and core app
* Static files setup and ready
* Nginx for reverse proxy

## Installation

```bash
git clone https://github.com/riad-azz/django-template.git
```

## Running the app

```bash
# development run
python manage.py runserver # host -> 127.0.0.1:8000

# production build
docker-compose -f docker-compose.yml up -d --build

# production run
docker-compose -f docker-compose.yml up -d

# production stop
docker-compose -f docker-compose.yml down
```

Make sure to run collectstatic before production

```
python manage.py collectstatic
```