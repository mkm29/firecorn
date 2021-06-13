""" Enforce validation with Pydantic and map Inputs and Outputs to API"""

from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType

# pylint: disable=no-name-in-module
from pydantic import BaseModel


class CommentsModel(BaseModel):
    """Pydantic BaseModel for Comments"""

    id: int
    user_id: int
    post_id: int
    body: str


class PostModel(BaseModel):
    """Pydantic BaseModel for Post"""

    id: int
    user_id: int
    title: str
    body: str
    comments: Optional[List[CommentsModel]]


class UserModel(BaseModel):
    """Pydantic BaseModel for User"""

    id: int
    name: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[List[PostModel]]
    comments: Optional[List[CommentsModel]]


class CommentGrapheneModel(PydanticObjectType):
    """Output used in Comments GraphQL Comments endpoints"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = CommentsModel


class PostGrapheneModel(PydanticObjectType):
    """Output used in Comments GraphQL Post endpoints"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = PostModel


class UserGrapheneModel(PydanticObjectType):
    """Output used in Comments GraphQL User endpoints"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = UserModel


class CommentGrapheneInputModel(PydanticInputObjectType):
    """Input (Arguments) to GraphQL endpoint"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = CommentsModel
        exclude_fields = ("id",)


class PostGrapheneInputModel(PydanticInputObjectType):
    """Input (Arguments) to GraphQL endpoint"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = PostModel
        exclude_fields = ("id", "comments")


class UserGrapheneInputModel(PydanticInputObjectType):
    """Input (Arguments) to GraphQL endpoint"""

    class Meta:
        """Meta class specifying Pydantic model to use"""

        model = UserModel
        exclude_fields = ("id", "posts", "comments")
