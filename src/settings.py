from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY', cast=Secret)

DATABASES = {
    "postgres": {
        "driver": config("DB_DRIVER", default="sqlite"),
        "host": config("DB_HOST", default="localhost"),
        "database": config("DB_DATABASE", default="fastapi"),
        "user": config("DB_USER", default=None),
        "password": config("DB_PASSWORD", cast=Secret, default=None),
        "port": config("DB_PORT", cast=int, default=5432),
    }
}