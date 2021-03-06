""" Comments Mutations """

from graphene import Mutation

from src.serializers import CommentGrapheneInputModel, CommentGrapheneModel
from src.models.user import User
from src.models.post import Post
from src.models.comment import Comments


class CreateComment(Mutation):
    """Mutation for Creating a Comment"""

    class Arguments:
        """Endpoint Arguments for Mutation"""

        comment_details = CommentGrapheneInputModel()

    Output = CommentGrapheneModel

    @staticmethod
    def mutate(parent, info, comment_details):
        """Mutation Function that is called when endpoint is accessed"""

        user = User.find_or_fail(comment_details.user_id)
        post = Post.find_or_fail(comment_details.post_id)

        comment = Comments()
        comment.body = comment_details.body

        user.comments().save(comment)
        post.comments().save(comment)

        return comment
