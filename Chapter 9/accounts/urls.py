from django.urls import path, include

from .views import HomePage, SignUpView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='sign_up'),
]
