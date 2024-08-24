from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
def register(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.SignupForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def update_user_data(request):
    if request.method == 'POST'  and "update" in request.POST:
        form = forms.UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('User data updated')) 
    else:
        form = forms.UserEditForm(instance=request.user)
    return render(request, 'registration/account.html', {'form': form})
