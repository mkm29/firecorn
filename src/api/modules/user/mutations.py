from graphene import Mutation

from src.models.user import User
from src.serializers import UserGrapheneInputModel, UserGrapheneModel


class CreateUser(Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        user = User()
        user.name = user_details.name
        user.address = user_details.address
        user.phone_number = user_details.phone_number
        user.sex = user_details.sex

        user.save()

        return user
