import graphene
import graphene_django
from .types import TodoType
from ..core.models import Todo


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=False)
        content = graphene.String(required=False)
        completed = graphene.Boolean(required=False)

    todo = graphene.Field(TodoType)

    def mutate(self, info, **kwargs):
        title = kwargs.get("title")
        content = kwargs.get("content")
        completed = kwargs.get("completed")

        todo = Todo(title=title, content=content, completed=completed)
        todo.save()

        return CreateTodo(todo)


class TodoMutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()
