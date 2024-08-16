from .forms import SubscribeForm
from django.shortcuts import render, redirect

def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm()
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect('home')
    else:
        subscribe_form = SubscribeForm
    return {"subscribe_form":subscribe_form}