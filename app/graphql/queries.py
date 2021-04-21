import graphene
from ..core.models import Todo
from .types import TodoType


class TodoQueries(graphene.ObjectType):
    todo = graphene.Field(TodoType, id=graphene.ID())
    todos = graphene.List(TodoType)

    def resolve_todo(self, info, id):
        todo = Todo.objects.get(pk=id)

        return todo

    def resolve_todos(self, info):
        todos = Todo.objects.all().order_by("id").reverse()

        return todos
