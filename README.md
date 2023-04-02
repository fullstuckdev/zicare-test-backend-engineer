# Zicare Test Back-End Engineer

Zicare Test Back-End Engineer is a project created as a technical test for the back-end engineer position at Zicare. The project aims to test the ability to develop a back-end web application using FastAPI, as well as the ability to design and implement a database.

In this project, a simple API consisting of several endpoints will be created that can be used to access, add, update, and delete data from a PostgreSQL database. Additionally, a database schema will be created and migrations will be run to create the necessary tables.
## Daftar Isi

- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [License](#license)

## Installation

### Requirements

- Python 3.10+
- pip

### Clone Repository

```sh
$ git clone https://github.com/fullstuckdev/zicare-test-backend-engineer
$ cd 1. Technical test
$ cd app
```

### Install Dependencies

```sh
$ pip install uvicorn fastapi
$ pip install sqlalchemy
$ pip install psycopg2
```

### Change Config
```sh
- Change app/config.py -

DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/<your_database>'
```

## Usage

### Start Development Server

```sh
uvicorn main:app --reload
```

## Documentation

API documentation is available at: https://app.swaggerhub.com/apis/taufikmulyawan/zicare-test/1.0

Database Schema documentation is available at: https://dbdocs.io/taufikmulyawan/zicare

## License

This project is licensed under the MIT License.
