from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY', cast=Secret)

DATABASES = {
    "postgres": {
        "driver": config("DB_DRIVER", default="postgres"),
        "host": config("DB_HOST"),
        "database": config("POSTGRES_DB", default="fastapi"),
        "user": config("POSTGRES_USER", default=None),
        "password": config("POSTGRES_PASSWORD", cast=Secret, default=None),
        "port": config("DB_PORT", cast=int, default=5432),
    }
}