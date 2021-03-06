from django.urls import reverse_lazy
from django.views.generic import (DetailView, ListView, DeleteView, UpdateView,
                                  CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Custom Code
from .models import ArticleModel


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list_page.html'
    model = ArticleModel
    context_object_name = 'article_list'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article_detail_page.html'
    model = ArticleModel
    context_object_name = 'article'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'article_delete_page.html'
    model = ArticleModel
    success_url = reverse_lazy('article_list_url')
    context_object_name = 'article'

    def test_func(self):
        """Allow User to display the Article
            only if method return True
        """
        user = self.get_object()
        """Get current Article instance
        """
        return user.author == self.request.user
        """Return true if logged-in user is the same as Article author
        """


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'article_edit_page.html'
    model = ArticleModel
    fields = ('title', 'body')
    context_object_name = 'article'

    def test_func(self):
        """Allow User to display the Article
            only if method return True
        """
        user = self.get_object()
        """Get current Article instance
        """
        return user.author == self.request.user
        """Return true if logged-in user is the same as Article author
        """


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create_page.html'
    model = ArticleModel
    fields = ('title', 'body')
    context_object_name = 'article'

    def form_valid(self, form):
        """ Overwrite form validation method
        
                Code flow:
                    0. Pass `Form` as method argument
                    1. Set up current logged in user, as `Form`'s author
                    2. Revoke not overwriten form validation method,
                        passing `Form` as method argument
                         
        """
        form.instance.author = self.request.user
        return super().form_valid(form)