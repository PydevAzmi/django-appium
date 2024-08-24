from django.db import models
import uuid
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

PLATFORMS = (
    ('Android', _('Android')),
    ('iOS', _('iOS')),
    ('Other', _('Other')),
)

def apk_file_path(instance, file_name):
    return f"files/{instance.user}/Applications/{instance}/{file_name}"

def app_file_path(instance, file_name):
    return f"files/{instance.application.user}/Applications/{instance}/{instance.test_title}/{file_name}"


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    logo = models.ImageField(_("Banner"), upload_to=apk_file_path)
    user = models.ForeignKey(User, verbose_name=_("Owner"), related_name='apps', on_delete=models.CASCADE)
    apk_file = models.FileField(_("APK File"), upload_to=apk_file_path, max_length=100)
    platform = models.CharField(_("Platforrm"), max_length=50, choices=PLATFORMS)
    updated_at = models.DateTimeField(_("Time Updated At"), auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("app_detail", kwargs={"pk": self.pk})
    


class AppTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_title = models.CharField(_("Test Title"), max_length=50)
    application = models.ForeignKey(Application, verbose_name=_("Test"), related_name='tests', on_delete=models.CASCADE)
    tested_at = models.DateTimeField(_("Time Tested At"), auto_now=True)
    first_screen_screenshot =  models.FileField(_("screen 1"), upload_to=app_file_path, max_length=100, null=True, blank=True)
    second_screen_screenshot =  models.FileField(_("screen 2"), upload_to=app_file_path, max_length=100, null=True, blank=True)
    video =  models.FileField(_("video"), upload_to=app_file_path, max_length=100, null=True, blank=True)
    ui_hierarchy =  models.FileField(_("Ui Hierarchy"), upload_to=app_file_path, max_length=100, null=True, blank=True)
    screen_changed = models.BooleanField(_("Screen Changed"), default=False)
    
    class Meta:
        ordering = ['-tested_at']

    def __str__(self):
        return f'{self.test_title}'
    
    def get_absolute_url(self):
        return reverse("test_detail", kwargs={"pk": self.pk})
    
class SubscripedEmail(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    email = models.EmailField(_("Email"), max_length=254)
    def __str__(self):
        return f'{self.email}'