from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    nickname = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'nickname', 'email', 'password1', 'password2']
