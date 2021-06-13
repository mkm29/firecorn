""" Comments Queries """

from graphene import ObjectType, List, Field, NonNull, Int

from src.serializers import CommentGrapheneModel
from src.models.comment import Comments


class CommentsQueries(ObjectType):
    """Comments queries"""

    get_comment = Field(CommentGrapheneModel, comment_id=NonNull(Int))
    get_comments = List(CommentGrapheneModel)

    @staticmethod
    def resolve_get_comment(parent, info, comment_id):
        """Data resolver to get a single comment given a comment_id"""

        return Comments.find_or_fail(comment_id)

    @staticmethod
    def resolve_get_comments(parent, info):
        """Data resolver to get all comments"""

        return Comments.all()
