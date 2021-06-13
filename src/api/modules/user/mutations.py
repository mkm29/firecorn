""" User Mutations """

from graphene import Mutation

from src.models.user import User
from src.serializers import UserGrapheneInputModel, UserGrapheneModel


class CreateUser(Mutation):
    """Mutation for Creating a User"""

    class Arguments:
        """Endpoint Arguments for Mutation"""

        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        """Mutation Function that is called when endpoint is accessed"""

        user = User()
        user.name = user_details.name
        user.address = user_details.address
        user.phone_number = user_details.phone_number
        user.sex = user_details.sex

        user.save()

        return user
