from django.urls import path
from .views import hello_world

urlpatterns = [path('', hello_world, name='home')]
"""
'' - is a regex for empty string

hello_world - is function type object reference

'home' - is a name for the URL/regex pattern
"""
