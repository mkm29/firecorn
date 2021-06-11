from graphene import Mutation

from src.serializers import PostGrapheneModel, PostGrapheneInputModel
from src.models.user import User
from src.models.post import Post


class CreatePost(Mutation):
    class Arguments:
        post_details = PostGrapheneInputModel()

    Output = PostGrapheneModel

    @staticmethod
    def mutate(parent, info, post_details):
        user = User.find_or_fail(post_details.user_id)
        post = Post()
        post.title = post_details.title
        post.body = post_details.body

        user.posts().save(post)

        return post
