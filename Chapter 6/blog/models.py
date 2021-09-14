from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    """
    Create many-to-one relation with Django default User model
    """
    def __str__(self):
        return self.title
