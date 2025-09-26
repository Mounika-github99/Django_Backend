from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AuthUser  # your custom user model

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AuthUser  # use your custom model here
        fields = ("username", "email", "password1", "password2")
