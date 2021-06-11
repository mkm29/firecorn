# https://orator-orm.com/docs/0.8/basic_usage.html

<<<<<<< HEAD
# TODO - These need to be environment variables
DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "fastapi",
        "user": "fastapi",
        "password": "SuperSecretPassword",
        "prefix": "",
        "port": 5432
    }
}
=======
from orator import DatabaseManager, Schema, Model
from .settings import DATABASES
>>>>>>> 01-factory

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
