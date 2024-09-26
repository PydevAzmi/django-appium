from .forms import SubscribeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from .models import SubscripedEmail

def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST' and "subscribe" in request.POST:
        if request.user.is_anonymous:
            messages.warning(request, _('You need to login first'))
        else :  
            subscribe_form = SubscribeForm(request.POST)
            if subscribe_form.is_valid() and not request.user.is_anonymous:
                if not SubscripedEmail.objects.filter(user=request.user).exists():
                    subscribe = SubscripedEmail(
                        email = subscribe_form.cleaned_data["email"],
                        user = request.user)
                    subscribe.save()
                    messages.success(request, _('You have been subscribed in newsletter'))
                else:
                    messages.warning(request, _('You Are Already subscribed!'))
   
    return {"subscribe_form":subscribe_form}