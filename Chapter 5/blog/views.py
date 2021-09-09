from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


class HomePage(ListView):
    template_name = "index.html"
    model = Post
