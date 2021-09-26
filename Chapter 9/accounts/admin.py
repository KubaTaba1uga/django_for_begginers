# Django dependencies
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Custom dependencies
from .forms import CustomUserCreateForm, CustomUserUpdateForm
from .models import CustomUserModel


class CustomUserModelAdmin(UserAdmin):
    """
    Extend `UserAdmin` to use `CustomUserModel` when creating admin accounts
    """
    add_form = CustomUserCreateForm
    form = CustomUserUpdateForm
    model = CustomUserModel
    list_display = [
        'email',
        'username',
        'is_staff',
        'age',
    ]
    """
    Add capabability to display properties in admin-portal
    """
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age', )}), )
    """
    Add capability to update, upper fields in admin-portal
    """
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', )}), )
    """
    Add capability to create, using upper fields in admin-portal
    """


admin.site.register(CustomUserModel, CustomUserModelAdmin)
"""
Tell Django to show `CustomUserModel` inside admin-portal
"""