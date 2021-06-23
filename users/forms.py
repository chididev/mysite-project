from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# this is the user registeration form
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    nickname = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)

# handles tthe order which the fields are displayed on the page and specifies the model which users are saved to
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'nickname', 'email', 'password1', 'password2']
