from orator import DatabaseManager, Schema, Model

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

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)