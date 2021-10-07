from django.views.generic import (DetailView, ListView)
# Custom Code
from .models import ArticleModel


class ArticleListView(ListView):
    template_name = 'article_list_page.html'
    model = ArticleModel
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    template_name = 'article_detail_page.html'
    model = ArticleModel
    context_object_name = 'article'
