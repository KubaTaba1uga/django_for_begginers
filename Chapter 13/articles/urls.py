from django.urls import path
from .views import (ArticleDetailView, ArticleListView, ArticleDeleteView,
                    ArticleEditView, ArticleCreateView)

urlpatterns = [
    path('article/', ArticleListView.as_view(), name='article_list_url'),
    path('article/<int:pk>',
         ArticleDetailView.as_view(),
         name='article_detail_url'),
    path('article/<int:pk>/delete',
         ArticleDeleteView.as_view(),
         name='article_delete_url'),
    path('article/<int:pk>/edit',
         ArticleEditView.as_view(),
         name='article_edit_url'),
    path('article/new', ArticleCreateView.as_view(), name='article_create_url')
]