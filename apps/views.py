from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application, AppTest
from django.db.models import Q

def home(request):
    return render(request, 'apps/home.html')

class AppList(LoginRequiredMixin, ListView):
    model = Application
    paginate_by = 10
    template_name = 'apps/apps.html'
    def get_queryset(self):
        app_list = Application.objects.filter(user=self.request.user)
        return app_list

class TestList(LoginRequiredMixin, ListView):
    model = AppTest
    paginate_by = 10
    template_name = 'apps/tests.html'
    def get_queryset(self):
        test_list = AppTest.objects.filter(application__user=self.request.user)
        return test_list

