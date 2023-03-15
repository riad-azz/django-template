# DJANGO TEMPLATE

A social media where people can rant about their problems

## Development

* Docker development environment build
```
docker-compose -f docker-compose.dev.yml --env-file .env.dev up -d --build
```

* Docker development environment run
```
docker-compose -f docker-compose.dev.yml --env-file .env.dev up -d
```

* Docker development environment stop
```
docker-compose -f docker-compose.dev.yml down
```

## Production

* Docker production environment build
```
docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d --build
```

* Docker production environment run
```
docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d
```

* Docker production environment stop
```
docker-compose -f docker-compose.prod.yml down
```