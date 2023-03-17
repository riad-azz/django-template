# DJANGO TEMPLATE

Simple django starter template set up with docker ready for development and production.

it includes :
* Allauth for user management
* Email confirmation
* Django corsheaders
* Docker environment for DEVELOPMENT & PRODUCTION
* Postgresql Database
* Base html template and core app
* Static files setup and ready
* Nginx ready for reverse proxy

## Development

* Docker development environment build
```
docker-compose -f docker-compose.dev.yml up -d --build
```

* Docker development environment run
```
docker-compose -f docker-compose.dev.yml up -d
```

* Docker development environment stop
```
docker-compose -f docker-compose.dev.yml down
```

## Production

* Before production make sure to run the code
```
python manage.py collectstatic
```

* Docker production environment build
```
docker-compose -f docker-compose.prod.yml up -d --build
```

* Docker production environment run
```
docker-compose -f docker-compose.prod.yml up -d
```

* Docker production environment stop
```
docker-compose -f docker-compose.prod.yml down
```