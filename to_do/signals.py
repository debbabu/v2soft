from .models import *
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    post_delete
)
from django.core.exceptions import ValidationError
@receiver(pre_save, sender="to_do.ToDoList")
def todo_pre_save(sender, instance, *args, **kwargs):
    print(args)
    print(kwargs)
    if not instance.user:
        raise ValidationError("User Required")
    # else:

