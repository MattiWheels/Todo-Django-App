from django.db import models

# When called, create a TextField object that will store data in the
# todo_todoitem table of the db file in the main directory.

class TodoItem(models.Model):
    content = models.TextField()
    time = models.TextField()
    todolist = models.IntegerField(default=0)