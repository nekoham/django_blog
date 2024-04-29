from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.role

class Users(AbstractUser):
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL(), help_text="role of the user")
