from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your full name.')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your phone number.')
    address = forms.CharField(widget=forms.Textarea, required=True, help_text='Required. Enter your address.')

    class Meta:
        model = User
        fields = ['username', 'full_name', 'phone_number', 'address', 'password1', 'password2']
