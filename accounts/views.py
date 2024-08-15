from django.shortcuts import render, redirect
from . import forms

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
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.UserForm()
    return render(request, 'registration/account.html', {'form': form})