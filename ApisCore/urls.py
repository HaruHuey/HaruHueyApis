# HaruHueyApis/DatabasePy/urls.py

from django.urls import path
from ApisCore.views import test

urlpatterns = [
    # path('test', test, name='test')
    path('test', test, name='test')
]