""" Database model specification for User"""

from orator.orm import has_many

from ..db import Model

# pylint: disable=import-error
from .post import Post

# pylint: disable=import-error
from .comment import Comments


class User(Model):
    """User database model"""

    @has_many
    # pylint: disable=no-self-use
    def posts(self):
        """One user can have many posts"""

        return Post

    @has_many
    # pylint: disable=no-self-use
    def comments(self):
        """One User can have many Comments"""

        return Comments
