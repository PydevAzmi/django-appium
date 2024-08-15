from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class UserForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ['first_name' , 'last_name', 'email' ]
