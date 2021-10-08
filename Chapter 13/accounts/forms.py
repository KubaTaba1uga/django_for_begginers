from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel

USER_EDITABLE_FIELDS = (
    'username',
    'email',
)


class CustomUserCreateForm(UserCreationForm):
    """User creation form
    """
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = USER_EDITABLE_FIELDS


class CustomUserUpdateForm(UserChangeForm):
    """User update form
    """
    class Meta:
        model = CustomUserModel
        fields = USER_EDITABLE_FIELDS
