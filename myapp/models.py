from django.db import models
from django.utils import timezone


class Todolist(models.Model):
    todo = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

