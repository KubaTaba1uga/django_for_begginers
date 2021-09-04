from django.db import models


class Post(models.Model):
    content = models.TextField()
    title = models.TextField(max_length=32)

    def __str__(self) -> str:
        """
        represent Post instance preview in 'Django administration' portal
        """
        return self.content[:50]