from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
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


class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('post_show_all')
    """
    After URL completion, wait until deletion end
    with executing redirection
    """