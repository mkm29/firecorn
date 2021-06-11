from graphene import Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from .api.schema import Query, Mutation

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))

@app.get('/')
def ping():
    return {'ping': 'pong'}