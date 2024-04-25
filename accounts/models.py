from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
