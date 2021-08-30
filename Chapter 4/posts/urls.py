from .views import PostsBoard
from django.urls import path

urlpatterns = [path('', PostsBoard.as_view(), name='posts')]
