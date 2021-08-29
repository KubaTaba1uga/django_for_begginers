from django.urls import path

from .views import HelloWorld, AboutMe

urlpatterns = [
    path('hello_world', HelloWorld.as_view(), name='hello_world'),
    path('about_me', AboutMe.as_view(), name='about_me')
]
