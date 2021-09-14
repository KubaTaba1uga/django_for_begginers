from django.urls import path
from .views import HomePage, PostDetails

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('post/<int:pk>', PostDetails.as_view(), name='')
]
"""
primary key (id) of bounded model is passed to View as integer, if value is preceded with /post
"""