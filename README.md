# DJANGO TEMPLATE

Simple django starter template set up with docker ready for development and production.

it includes :
* Allauth for user management
* Email confirmation
* Django corsheaders
* Docker environment for **Development** & **Production**
* Postgresql Database
* Base html template and core app
* Static files setup and ready
* Nginx for reverse proxy

## Installation

```bash
git clone https://github.com/riad-azz/django-template.git
```

## Running the project

### Development

```bash
#development build
docker-compose -f docker-compose.dev.yml up -d --build

# development run
docker-compose -f docker-compose.dev.yml up -d

# development stop
docker-compose -f docker-compose.dev.yml down
```

### Production

Make sure to run collectstatic before production

```
python manage.py collectstatic
```

```bash
#development build
docker-compose -f docker-compose.dev.yml up -d --build

# development run
docker-compose -f docker-compose.dev.yml up -d

# development stop
docker-compose -f docker-compose.dev.yml down
```