# HaruHueyApis/KakaoApi/urls.py

from django.urls import path

from KakaoApi.views import *

urlpatterns = [
    path('KakaoApi_GoodCoin_First', KakaoApi_GoodCoin_First, name='KakaoApi_GoodCoin_First'),
    path('oauth', oauth_kakao, name='oauth_kakao'),
    path('Meal', Meal, name='Meal'),
    path('Weather', Weather, name='Weather'),
    path('AirData', AirData, name='AirData'),
    path('AirMise', AirMise, name='AirMise'),
    path('AirMise_forecast', AirMise_forecast, name='AirMise_forecast'),
    path('SchoolInfo', SchoolInfo, name='SchoolInfo'),
    path('DepartmentInfo', DepartmentInfo, name='DepartmentInfo'),
    path('SchoolData', SchoolData, name='SchoolData'),
    # path('GoodCoin', GoodCoin_API, name='GoodCoin')
]