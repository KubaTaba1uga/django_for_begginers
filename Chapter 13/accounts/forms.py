from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db import models

from .models import CustomUserModel


class CustomUserCreateForm(UserCreationForm):
    """User creation form
    """
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields


class CustomUserUpdateForm(UserChangeForm):
    """User update form
    """
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields
