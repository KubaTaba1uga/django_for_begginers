from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    """
    Create many-to-one relation with Django default User model
    """
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Location of each post entry is 'post' URL appended with its id
        This method is required by a CreateView
        """
        return reverse('post_show_details', args=[str(self.id)])
        """                        
        Reference the URL object by it's name
        & pass (to URL object) model instance id, as an argument.
        URL is executed immediately after creation
        """

