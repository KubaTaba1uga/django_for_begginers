from django.urls import path
from .views import hello_world

urlpatterns = [path('hello_world', hello_world.as_view(), name='hello_world')]
