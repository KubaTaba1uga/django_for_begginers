from django.urls import path
from .views import SignUp

urlpatterns = [path('sign_up', SignUp.as_view(), name='user_sign_up')]
