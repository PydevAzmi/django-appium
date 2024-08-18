from .forms import SubscribeForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import SubscripedEmail

def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            if not SubscripedEmail.objects.filter(user=request.user).exists():
                subscribe = SubscripedEmail(
                    email = subscribe_form.cleaned_data["email"],
                    user = request.user)
                subscribe.save()
                messages.success(request, 'You have been subscribed in newsletter')
            else:
                messages.warning(request, 'You Are Already subscribed!')
    return {"subscribe_form":subscribe_form}