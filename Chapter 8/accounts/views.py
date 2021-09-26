from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from .forms import CustomUserCreateForm


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home_page.html")


class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'