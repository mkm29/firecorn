# FireCorn

[![Install Dependencies, Check Quality and Run Tests](https://github.com/mkm29/firecorn/actions/workflows/test.yaml/badge.svg)](https://github.com/mkm29/firecorn/actions/workflows/test.yaml)
[![Security Scan](https://github.com/mkm29/firecorn/actions/workflows/scan.yaml/badge.svg)](https://github.com/mkm29/firecorn/actions/workflows/scan.yaml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mkm29_firecorn&metric=coverage)](https://sonarcloud.io/dashboard?id=mkm29_firecorn)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mkm29_firecorn&metric=alert_status)](https://sonarcloud.io/dashboard?id=mkm29_firecorn)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

![FireCorn](media/firecorn.jpeg)

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

## Docker-compose

I have included a `docker-compose.yml` file that will start a `PostgreSQL 12` instance, all you need to do is run `docker-compose up --build -d` and access the API at `http://localhost:8080`

## Tests

Run tests with: `python -m pytest -s tests`. Currently there are 9 tests: 3 for User, Post and Comments, and coverage is at `100%`.

### Example Mutations/Queries

```javascript
mutation createUser {
  createUser(userDetails: {
    name: "John Doe",
    address: "Some address",
    phoneNumber: "12345678",
    sex: "male"
  })
  {
    id
    name
    posts {
      body
      comments {
        body
      }
    }
  }
}

mutation createPost {
  createPost(postDetails: {
    userId: 1,
    title: "My first Post",
    body: "This is a Post about myself"
  })
  {
    id
  }
}

mutation createComment {
  createComment(commentDetails: {
    userId: 1,
    postId: 1,
    body: "Another Comment"
  })
  {
    id
    body
  }
}

query getUser {
  getUser(userId: 1) {
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```

_todo_: **note 1**
