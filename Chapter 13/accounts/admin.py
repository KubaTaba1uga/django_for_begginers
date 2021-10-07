from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserUpdateForm
from .models import CustomUserModel


class CustomUserModelAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserUpdateForm
    model = CustomUserModel


admin.site.register(CustomUserModel, CustomUserModelAdmin)
