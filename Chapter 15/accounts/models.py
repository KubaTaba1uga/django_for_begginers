from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserModel(AbstractUser, TimeStamps):
    pass
