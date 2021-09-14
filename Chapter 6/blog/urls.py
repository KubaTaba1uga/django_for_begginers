from django.urls import path
from .views import HomePage, PostCreate, PostDetails, PostUpdate

urlpatterns = [
    path('', HomePage.as_view(), name='post_show_all'),
    path('post/<int:pk>', PostDetails.as_view(), name='post_show_details'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('post/new', PostCreate.as_view(), name='post_create')
]
"""
primary key (id) of bounded model is passed to View as integer, if value preceded with /post
"""