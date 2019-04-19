# HaruHueyApis/DialogflowApi/urls.py

from django.urls import path

from DialogflowApi.views import Apis_Views

urlpatterns = [
    # path('test', test, name='test')
    path('Apis_Views', Apis_Views, name='Apis_Views')
]