""" Database model specification for Post"""

from orator.orm import has_many

from ..db import Model

# pylint: disable=import-error
from .comment import Comments


class Post(Model):
    """Specify any relations here"""

    @has_many
    # pylint: disable=no-self-use
    def comments(self):
        """One blog Post can have many comments"""

        return Comments
