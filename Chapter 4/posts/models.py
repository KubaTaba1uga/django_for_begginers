from django.db import models


class Post(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        """
        represent Post instance preview in 'Django administration' portal
        """
        return self.content[:50]