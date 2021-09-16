from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = UserCreationForm
    """
    Specify the use of built-in "UserCreationForm" form class
    """
    success_url = reverse_lazy('login')
    """
    Specify URL which redirection is pointing to, after login successfully
    """
    template_name = 'registration/signup.html'