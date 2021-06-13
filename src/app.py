"""Module to create FastAPI application"""

from graphene import Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

# pylint: disable=import-error
from .api.schema import Query, Mutation


def create_app(debug=False):
    """Factory method to create FastAPI application"""

    app = FastAPI(debug=debug)

    app.add_route("/", GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))
    return app
