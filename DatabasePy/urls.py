# HaruHueyApis/DatabasePy/urls.py

from django.urls import path
from DatabasePy.views import CallTest

urlpatterns = [
    # path('test', test, name='test')
    path('calltest', CallTest)
]