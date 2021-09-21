from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import CustomUserModel


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('age', )
        """
        Add  custom field to `CustomUserModel` 
        """


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields
        """
        This is space for `CustomUserModel` custom fields 
        """
