from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 변경
def test():
    return HttpResponse("ApisCore")