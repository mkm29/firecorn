from graphene import ObjectType, List, Field, NonNull, Int

from src.serializers import PostGrapheneModel
from src.models.post import Post


class PostQueries(ObjectType):
    """Post queries"""

    get_post = Field(PostGrapheneModel, post_id=NonNull(Int))
    get_posts = List(PostGrapheneModel)

    @staticmethod
    def resolve_get_post(parent, info, post_id):
        return Post.find_or_fail(post_id)

    @staticmethod
    def resolve_get_posts(parent, info):
        return Post.all()
