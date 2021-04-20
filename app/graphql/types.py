import graphene
from graphene_django import DjangoObjectType
from ..core.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
