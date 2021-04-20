import graphene
import graphene_django


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=False)
        content = graphene.String(required=False)
        completed = graphene.Boolean(required=False)

