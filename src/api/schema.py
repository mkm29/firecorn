from graphene import ObjectType, String

from .modules.comment.mutations import CreateComment
from .modules.post.mutations import CreatePost
from .modules.user.mutations import CreateUser
from .modules.user.queries import UserQueries


class Query(UserQueries):
    """Queries"""


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
