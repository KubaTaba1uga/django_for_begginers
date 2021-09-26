from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = ('username', ) + ('age', ) + ('email', )
        """
        Include 'age', 'email' & 'username' in sign-up form 
        """


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ('email', )
        """
        Include 'email' in User update form 
        """
