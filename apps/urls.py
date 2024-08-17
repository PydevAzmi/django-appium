from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('apps/',views.AppList.as_view(), name='apps'),
    path('test/',views.TestList.as_view(), name='tests'),
]
