import graphene
from .queries import TodoQueries
from .mutations import TodoMutations


class RootQuery(TodoQueries, graphene.ObjectType):
    pass


class RootMutation(TodoMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
