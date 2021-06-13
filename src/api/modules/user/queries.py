""" User Queries """

from graphene import ObjectType, List, Field, NonNull, Int

from src.serializers import UserGrapheneModel
from src.models.user import User


class UserQueries(ObjectType):
    """User queries"""

    get_user = Field(UserGrapheneModel, user_id=NonNull(Int))
    get_users = List(UserGrapheneModel)

    @staticmethod
    def resolve_get_user(parent, info, user_id):
        """ Data resolver to get a single User given a user_id """

        return User.find_or_fail(user_id)

    @staticmethod
    def resolve_get_users(parent, info):
        """ Data resolver to get all Users """

        return User.all()
