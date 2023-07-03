# Tech Assessment

Application for data processing from csv or excel file that maps information to a centralize database using django 4 and djangorestframework 3.14.

## Requirements

#### Dockerized application:

- Virtualization Capabilities - As docker needs virtualization in the host computer to work.
- Docker & Docker Compose properly installed.

#### Local instalation:
- Python version 3.10
- Postgres 13
- psycopg2 (python database engine to work with postgres)
- C and C++ compiler and standard library (libgcc & libstdc++ for linux apline) as they are used by Pandas library.

## Installation

### Docker

```sh
docker-compose build # Creates the app and postgres images
docker-compose run --rm app sh -c "python manage.py migrate" # Recomended to apply migrations before start application
docker-compose up # Starts the application in port 8000
```
`docker-compose up` starts the database and the application server. It also applies the migration, the `wait_for_db` command not always work the first time the project start as the database volume is not created already, so if is the first time that the project starts is recommended to use the `docker-compose run --rm app sh -c "python manage.py migrate"` command first.

### For local environment:

Is recomended to use a python virtual environment for these steps and have a running postgres database.

Create a .env file that contain the database information:
`DB_HOST=<database-host>`
`DB_NAME=<database-name>`
`DB_USER=<database-user>`
`DB_PASS=<database-password>`

```
pip install -r requirements.txt # Install all python dependencies.
python manage.py migrate # Apply all migrations to the database.
python manage.py runserver # Starts the application in localhost:8000
```

When the project is already started you can go to /api/docs/ to get the Swagger API documentation of the available endpoints.

## Plugins

| Plugin | Description |
| ------ | ------ |
| drf-spectacular | Django rest framework plugin for Swagger integration. |

