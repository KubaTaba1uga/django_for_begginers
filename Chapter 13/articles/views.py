from django.urls import reverse_lazy
from django.views.generic import (DetailView, ListView, DeleteView, UpdateView)
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


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete_page.html'
    model = ArticleModel
    success_url = reverse_lazy('article_list_url')
    context_object_name = 'article'


class ArticleEditView(UpdateView):
    template_name = 'article_edit_page.html'
    model = ArticleModel
    fields = ('title', 'body')
    context_object_name = 'article'
