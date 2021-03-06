from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post


class HomePage(ListView):
    template_name = "index.html"
    model = Post


class PostDetails(DetailView):
    template_name = "post.html"

    model = Post
    """
    DetailView provide context object wich can be used in the template
    by 'post' or 'object' name
    """

    # context_object_name = "the_post"
    """
    Provide alternative name for context object
    """