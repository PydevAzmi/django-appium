from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    path('apps/',views.AppList.as_view(), name='apps'),
    path('apps/create/',views.AppCreate.as_view(), name='create_app'),
    path('apps/<pk>/',views.AppDetail.as_view(), name='app_detail'),
    path('apps/<pk>/update/',views.AppUpdate.as_view(), name='update_app'),
    path('apps/<pk>/delete/',views.AppDelete.as_view(), name='delete_app'),

    path('test/',views.TestList.as_view(), name='tests'),
    path('test/create/',views.TestCreate.as_view(), name='create_test'),
    path('test/<pk>/',views.TestDetail.as_view(), name='test_detail'),
    path('test/<pk>/update/',views.TestUpdate.as_view(), name='update_test'),
    path('test/<pk>/delete/',views.TestDelete.as_view(), name='delete_test'),
]
