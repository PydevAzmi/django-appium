from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application, AppTest
from .forms import AppCreateForm, AppUpdateForm, TestUpdateForm, CapabilitiesForm


from appium import webdriver
import subprocess
import base64
import time
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput


def home(request):
    return render(request, 'apps/home.html')


class AppList(LoginRequiredMixin, ListView):
    model = Application
    paginate_by = 10
    template_name = 'apps/apps.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppCreateForm
        return context

    def get_queryset(self):
        app_list = Application.objects.filter(user=self.request.user)
        return app_list


class AppCreate(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'apps/apps.html'
    success_url = '/apps'
    fields = [
            "name",
            "logo",
            "apk_file",
            "platform",
            "description",
        ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AppDetail(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'apps/app_detail.html'
    success_url = '/apps'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = Application.objects.get(pk = self.kwargs['pk'], user=self.request.user)
        context['form'] = AppUpdateForm(instance=instance)
        context['caps_form'] = CapabilitiesForm()
        return context


class AppUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    template_name = 'apps/app_detail.html'
    fields = [
            "name",
            "description",
            "platform",
        ]
    

class AppDelete(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'apps/app_detail.html'
    success_url = '/apps'



class TestCreate(LoginRequiredMixin, CreateView):
    model = AppTest
    template_name = 'apps/tests.html'
    success_url = '/tests'
    fields = "__all__"
    
    def post(self, form):
        print("Valid")
        #`Write Logic`
        return super().post(form)


class TestList(LoginRequiredMixin, ListView):
    model = AppTest
    paginate_by = 10
    template_name = 'apps/tests.html'
    
    def get_queryset(self):
        test_list = AppTest.objects.filter(application__user=self.request.user)
        return test_list

class TestDetail(LoginRequiredMixin, DetailView):
    model = AppTest
    context_object_name = "test"
    template_name = 'apps/test_detail.html'
    success_url = '/tests/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = AppTest.objects.get(pk = self.kwargs['pk'])
        context['form'] = TestUpdateForm(instance=instance)
        return context


class TestUpdate(LoginRequiredMixin, UpdateView):
    model = AppTest
    fields = ["test_title",]
    template_name = 'apps/test_detail.html'
    

class TestDelete(LoginRequiredMixin, DeleteView):
    model = AppTest
    template_name = 'apps/test_detail.html'
    success_url = '/tests/'



