from django.db import models
from users.models import User

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='to_do_user', null=True, blank=True)
    item = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)