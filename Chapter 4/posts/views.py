from django.views.generic import ListView
from .models import Post


class PostsBoard(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'last_posts'
    """
    alias for template engine
    in html file class is represented as 'last_posts'
    """