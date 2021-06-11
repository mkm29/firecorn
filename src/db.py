# https://orator-orm.com/docs/0.8/basic_usage.html

from orator import DatabaseManager, Schema, Model
from .settings import DATABASES

db = DatabaseManager(DATABASES.get('postgres'))
schema = Schema(db)
Model.set_connection_resolver(db)
