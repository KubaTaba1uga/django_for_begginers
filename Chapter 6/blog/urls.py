from django.urls import path
from .views import HomePage, PostCreate, PostDetails

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('post/<int:pk>', PostDetails.as_view(), name='post'),
    path('post/new', PostCreate.as_view(), name='new_post')
]
"""
primary key (id) of bounded model is passed to View as integer, if value preceded with /post
"""