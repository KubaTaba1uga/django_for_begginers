from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStamps(models.Model):
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserModel(AbstractUser, TimeStamps):
    age = models.PositiveIntegerField(null=True, blank=True)