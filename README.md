# SuperFast (simple) Blog

```yaml
Author: Mitchell Murphy
Date: 11 June 2021
Version: 0.1.0
```

## Introduction

This project is a very simple blog GraphQL API that uses FastAPI, Starlette, Orator, Graphene and Uvicorn. A Dockerfile is provided, in order to use this app you either need to override the database environment variables to use SQLite or create a PostgreSQL database (and user), and then run the migrations as so: `cd src && orator migrate -c db.py`.

## Dependency Management

This app uses the [Poetry](https://python-poetry.org/) Python packaging and dependency management system. If you would like to run this application locally (it is recommended that you use the included Dockerfile), you need to create a virtual environment and install the dependencies as so:

```shell
poetry shell
poetry install
```

## Run

This application can be run locally or via Docker (suggested). To run locally (after entering the virtual environment as instructed above), issue the following command: `uvicorn --factory src.app:create_app --reload --port 8080`

### Docker

```shell
docker build -t superfast/blog:0.1.0 .
docker run --rm -it -p 8080:8080 superfast/blog:0.1.0
```
