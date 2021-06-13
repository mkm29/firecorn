"""Database module, using Orator ORM"""

# https://orator-orm.com/docs/0.8/basic_usage.html

from orator import DatabaseManager, Schema, Model

# pylint: disable=import-error
from .settings import DATABASES

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
