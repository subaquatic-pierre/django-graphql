from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True)

