from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import UserModel


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class UserLoginForm(AuthenticationForm):
    username = None
    email = forms.EmailField(required=True)