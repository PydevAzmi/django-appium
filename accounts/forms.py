from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2']

class UserEditForm(UserChangeForm):
    password = forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly', 'value':'*******'}))
    username =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User 
        fields = ['username','first_name' , 'last_name', 'email']
