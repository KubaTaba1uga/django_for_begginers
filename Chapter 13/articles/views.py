from django.shortcuts import render
from django.views.generic import DetailView
# Custom Code
from .models import ArticleModel


class ArticleDetailView(DetailView):
    template_name = 'article_detail_page.html'
    model = ArticleModel
