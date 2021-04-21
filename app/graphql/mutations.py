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


class EditTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=False)
        content = graphene.String(required=False)
        completed = graphene.Boolean(required=False)

    todo = graphene.Field(TodoType)

    def mutate(self, info, **kwargs):
        id = kwargs.get("id")
        title = kwargs.get("title")
        content = kwargs.get("content")
        completed = kwargs.get("completed")

        todo = Todo.objects.get(pk=id)
        if title:
            todo.title = title
        if content:
            todo.content = content
        if completed:
            todo.completed = completed

        todo.save()

        return EditTodo(todo)


class DeleteTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    deleted = graphene.Field(graphene.Boolean)

    def mutate(self, info, id):
        todo = Todo.objects.get(pk=id)
        todo.delete()

        return DeleteTodo(deleted=True)


class TodoMutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    edit_todo = EditTodo.Field()
    delete_todo = DeleteTodo.Field()
