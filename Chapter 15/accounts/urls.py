from os import name
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import SignUpView

URL_PREFIX = 'accounts/'

urlpatterns = [
    path(URL_PREFIX, include('django.contrib.auth.urls')),
    path(URL_PREFIX+'signup/', SignUpView.as_view(), name='signup'),
    path(URL_PREFIX+'password/success', PasswordChangeDoneView.as_view(template_name='registration/password/password_edit_success_page.html'),name='password_edit_success_url'),
    path(URL_PREFIX+'password/edit', PasswordChangeView.as_view(template_name='registration/password/password_edit_form_page.html', success_url=reverse_lazy('password_edit_success_url')), name='password_edit_url')
]
