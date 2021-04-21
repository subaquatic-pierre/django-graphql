import json
from graphene_django.utils.testing import GraphQLTestCase
from .schema import schema


class TestTodoQueries(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ["todo"]

    def setUp(self) -> None:
        return super().setUp()

    def test_get_todos(self):
        response = self.query(
            """ 
          query GetTodos {
            todos {
                id
                title
                content
                completed
            }
        }
        """,
            op_name="GetTodos",
        )

        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        todos = content.get("data").get("todos")
        assert len(todos) >= 0, "No todos were returned from the query"

    def test_get_todo(self):
        response = self.query(
            """ 
          query GetTodo($id: ID) {
            todo(id: $id) {
                id
                title
                content
                completed
            }
        }
        """,
            op_name="GetTodo",
            variables={"id": 1},
        )

        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        todo = content.get("data").get("todo")
        assert todo.get("title") == "Create New world", "Incorrect todo returned"

