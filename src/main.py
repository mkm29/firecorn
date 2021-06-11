from graphene import Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from .api.schema import Query, Mutation

app = FastAPI()

app.add_route("/api", GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))
