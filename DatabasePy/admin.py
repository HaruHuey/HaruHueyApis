from django.contrib import admin
from DatabasePy.models import Weather_skplanet, Weather_skplanet_en
from DatabasePy.models import MealData_Neis, MealData_Neis_en, AirData_airkorea
from DatabasePy.models import Health_index, Living_index

# Register your models here.
admin.site.register(Weather_skplanet)
admin.site.register(Weather_skplanet_en)
admin.site.register(MealData_Neis)
admin.site.register(MealData_Neis_en)
admin.site.register(AirData_airkorea)
admin.site.register(Health_index)
admin.site.register(Living_index)