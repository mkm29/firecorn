from graphene import ObjectType, List, Field, NonNull, Int

from src.serializers import UserGrapheneModel
from src.models.user import User

class UserQueries(ObjectType):
    """ User queries """

    get_user = Field(UserGrapheneModel, user_id=NonNull(Int))
    get_users = List(UserGrapheneModel)

    @staticmethod
    def resolve_get_user(parent, info, user_id):
        return User.find_or_fail(user_id)

    @staticmethod
    def resolve_list_users(parent, info):
        return User.all()
