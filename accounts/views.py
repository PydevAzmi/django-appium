from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate , login
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.SignupForm()
    return render(request, 'registration/register.html', {'form': form})

def update_user_data(request):
    if request.method == 'POST':
        form = forms.UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = forms.UserEditForm(instance=request.user)
    return render(request, 'registration/account.html', {'form': form})
