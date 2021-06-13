""" Post Mutations """

from graphene import Mutation

from src.serializers import PostGrapheneModel, PostGrapheneInputModel
from src.models.user import User
from src.models.post import Post


class CreatePost(Mutation):
    """Mutation for Creating a Post"""

    class Arguments:
        """Endpoint Arguments for Mutation"""

        post_details = PostGrapheneInputModel()

    Output = PostGrapheneModel

    @staticmethod
    def mutate(parent, info, post_details):
        """Mutation Function that is called when endpoint is accessed"""

        user = User.find_or_fail(post_details.user_id)
        post = Post()
        post.title = post_details.title
        post.body = post_details.body

        user.posts().save(post)

        return post
