from django import forms
from .models import *

class SubscribeForm(forms.ModelForm):
    email = forms.EmailField( required=False)
    class Meta:
        model = SubscripedEmail
        fields = ['email']