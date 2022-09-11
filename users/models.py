from django.db import models
from django.contrib.auth.models import (
    AbstractUser,BaseUserManager
    )

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        if password:
            user.set_password(password)
            user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
class User(AbstractUser):
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)