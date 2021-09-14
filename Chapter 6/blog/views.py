from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from .models import Post


class HomePage(ListView):
    template_name = "post_all.html"
    model = Post


class PostDetails(DetailView):
    template_name = "post_details.html"

    model = Post
    """
    DetailView provide context object wich can be used in the template
    by 'post' or 'object' name
    """

    # context_object_name = "the_post"
    """
    Provide alternative name for context object
    """


class PostCreate(CreateView):
    template_name = 'post_create.html'

    model = Post
    """
    CreateView provide context object wich can be used in the template
    by 'form' name
    """

    fields = ['title', 'author', 'body']
    """
    Represent database fields which are exposed by template's form
    """


class PostUpdate(UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'body']
