from django.http import HttpResponse
from django.shortcuts import render
from DatabasePy.AirData_AirKorea.airdata_api import API_Call_AirData
from DatabasePy.MealData_Neis.mealdata_api import API_Call_MealData
from DatabasePy.Weather_index.Health_index import Health_index_Data
from DatabasePy.Weather_index.Living_index import Living_index_Data
from DatabasePy.Weather_skplanet.weather_skplanet_api import Weather_Skplanet

# 테스트
def CallTest(request):
    API_Call_MealData()
    Health_index_Data()
    Living_index_Data()
    Weather_Skplanet()
    calltest = API_Call_AirData()
    return HttpResponse(calltest)