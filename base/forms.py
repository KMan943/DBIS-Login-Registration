# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    phone_no = forms.CharField(max_length=15, required=True )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone_no']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        }


