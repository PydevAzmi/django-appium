from django import forms
import os
from django.core.exceptions import ValidationError
from .models import *
from django.utils.translation import gettext_lazy as _


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Extract the file extension
    valid_extensions = ['.apk']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only APK files are allowed.')

class SubscribeForm(forms.ModelForm):
    email = forms.EmailField( required=True)
    class Meta:
        model = SubscripedEmail
        fields = ['email']



class AppCreateForm(forms.ModelForm):
    apk_file = forms.FileField(validators=[validate_file_extension])
    class Meta:
        model = Application
        fields = [
            "name",
            "logo",
            "apk_file",
            "platform",
            "description",
        ]


class AppUpdateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "name",
            "description",
            "platform",
        ]

class TestUpdateForm(forms.ModelForm):
    class Meta:
        model = AppTest
        fields = [
            "test_title",
        ]


class CapabilitiesForm(forms.ModelForm):
    platform_name = forms.CharField(label=_("Paltform Name"), required=False, widget=forms.TextInput(attrs={'readonly':'readonly', 'value':_('Android')}))
    automation_name = forms.CharField(label=_('Automation Name'),required=False, widget=forms.TextInput(attrs={'readonly':'readonly', 'value':'uiautomator2'}))
    platform_version= forms.CharField(required=True,label=_('Paltform Version'))
    device_name= forms.CharField(required=True,label=_('Device Name'))
    language= forms.CharField(required=True,label=_('Language'))
    locale= forms.CharField(required=True,label=_('Locale'))
    first_button_xpath= forms.CharField(required=True,label=_('First Button XPath'))

    class Meta:
        model = AppTest
        fields = [
            "test_title"
        ]
