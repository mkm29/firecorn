from graphene import Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from .api.schema import Query, Mutation


def create_app(debug=False):
    app = FastAPI(debug=debug)

    app.add_route("/", GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))
    return app
