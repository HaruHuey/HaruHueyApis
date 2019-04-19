from django.db import models

# Create your models here.
# create = models.DateTimeField(auto_now_add=True)
# updated = models.DateTimeField(auto_now=True)

# Weather_skplanet ( 날씨 )
class Weather_skplanet(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 날짜
    Date = models.CharField(max_length=12)
    # 시간
    Time = models.CharField(max_length=7)
    # 관측소 정보
    station_name = models.CharField(max_length=15)
    # 관측소 유형
    station_type = models.CharField(max_length=8)
    # 바람 풍향
    wind_wdir = models.CharField(max_length=8)
    # 바람 풍속
    wind_wspd = models.CharField(max_length=5)
    # 1시간 누적 강수량 ( 눈과 비 통합 )
    snowrain_sinceOntime = models.CharField(max_length=5)
    # 강수형태 코드
    snowrain_type = models.CharField(max_length=1)
    # 하늘 상태
    sky_name = models.CharField(max_length=10)
    # 일 누적 강우량
    rain_sinceMidnight = models.CharField(max_length=5)
    # 현재 기온
    temperature_tc = models.CharField(max_length=8)
    # 오늘 최고 기온
    temperature_tmax = models.CharField(max_length=8)
    # 오늘 최저 기온
    temperature_tmin = models.CharField(max_length=8)
    # 상대습도
    humidity = models.CharField(max_length=8)
    # 기압
    pressure_surface = models.CharField(max_length=10)

# Weather_skplanet_en ( 날씨 ) 영어 버전
class Weather_skplanet_en(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 날짜
    Date = models.CharField(max_length=12)
    # 시간
    Time = models.CharField(max_length=7)
    # 관측소 정보
    station_name = models.CharField(max_length=30)
    # 관측소 유형
    station_type = models.CharField(max_length=8)
    # 바람 풍향
    wind_wdir = models.CharField(max_length=8)
    # 바람 풍속
    wind_wspd = models.CharField(max_length=5)
    # 1시간 누적 강수량 ( 눈과 비 통합 )
    snowrain_sinceOntime = models.CharField(max_length=5)
    # 강수형태 코드
    snowrain_type = models.CharField(max_length=1)
    # 하늘 상태
    sky_name = models.CharField(max_length=15)
    # 일 누적 강우량
    rain_sinceMidnight = models.CharField(max_length=5)
    # 현재 기온
    temperature_tc = models.CharField(max_length=8)
    # 오늘 최고 기온
    temperature_tmax = models.CharField(max_length=8)
    # 오늘 최저 기온
    temperature_tmin = models.CharField(max_length=8)
    # 상대습도
    humidity = models.CharField(max_length=8)
    # 기압
    pressure_surface = models.CharField(max_length=10)


# MealData_Neis ( 급식 )
class MealData_Neis(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 월
    Mon = models.CharField(max_length=200)
    # 화
    Tue = models.CharField(max_length=200)
    # 수
    Wed = models.CharField(max_length=200)
    # 목
    Thu = models.CharField(max_length=200)
    # 금
    Fri = models.CharField(max_length=200)
    # 토
    Sat = models.CharField(max_length=100)
    # 일
    Sun = models.CharField(max_length=100)

# MealData_Neis_en ( 급식 )
class MealData_Neis_en(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 월
    Mon = models.CharField(max_length=300)
    # 화
    Tue = models.CharField(max_length=300)
    # 수
    Wed = models.CharField(max_length=300)
    # 목
    Thu = models.CharField(max_length=300)
    # 금
    Fri = models.CharField(max_length=300)
    # 토
    Sat = models.CharField(max_length=150)
    # 일
    Sun = models.CharField(max_length=150)

# AirData_airkorea ( 대기환경정보 ) ko - en 공통
class AirData_airkorea(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 아황산가스
    Air_So2 = models.CharField(max_length=10)
    Air_So2_Context = models.CharField(max_length=40)
    # 일산화탄소
    Air_Co = models.CharField(max_length=10)
    Air_Co_Context = models.CharField(max_length=40)
    # 오존
    Air_O3 = models.CharField(max_length=10)
    Air_O3_Context = models.CharField(max_length=40)
    # 이산화질소
    Air_No2 = models.CharField(max_length=10)
    Air_No2_Context = models.CharField(max_length=40)
    # 미세먼지
    Air_PM10 = models.CharField(max_length=10)
    Air_PM10_Context = models.CharField(max_length=40)
    # 초미세먼지
    Air_PM25 = models.CharField(max_length=10)
    Air_PM25_Context = models.CharField(max_length=40)
    # 통합대기환경지수
    Air_Khai = models.CharField(max_length=10)
    Air_Khai_Context = models.CharField(max_length=200)

class AirData_airkorea_forecast(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)

    # 미세먼지
    Air_PM10_forecast = models.CharField(max_length=10)
    Air_PM10_forecast_Context = models.CharField(max_length=40)

    # 초미세먼지
    Air_PM25_forecast = models.CharField(max_length=10)
    Air_PM25_forecast_Context = models.CharField(max_length=40)

# Health_index ( 보건기상정보 ) ko - en 공통
class Health_index(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 감기 지수
    inflWho = models.CharField(max_length=10)
    # 천식 지수
    AsthmaWho = models.CharField(max_length=10)
    # 뇌졸중 지수
    BrainWho = models.CharField(max_length=10)
    # 피부 질환 지수
    SkinWho = models.CharField(max_length=10)
    # 꽃가루 농도 ( 참나무 )
    FlowerWoodyWho = models.CharField(max_length=10)
    # 꽃가루 농도 ( 소나무 )
    FlowerPineWho = models.CharField(max_length=10)
    # 꽃가루 농도 ( 잡초류 )
    FlowerWeedsWho = models.CharField(max_length=10)

# Living_index ( 생활기상정보 ) ko - en 공통
class Living_index(models.Model):
    # 현재 시간
    DateTime = models.CharField(max_length=18)
    # 식중독 지수
    fsnLife = models.CharField(max_length=10)
    # 체감 온도
    Senso_temLife = models.CharField(max_length=10)
    # 열 지수
    HeatLife = models.CharField(max_length=10)
    # 불쾌 지수
    DsplsLife = models.CharField(max_length=10)
    # 자외선 지수
    UltrvLife = models.CharField(max_length=10)
    # 동파 가능 지수
    WinterLife = models.CharField(max_length=10)
    # 대기 확산 지수
    AirpllutionLife = models.CharField(max_length=10)
    # 더위 체감 지수
    Senso_HeatLife = models.CharField(max_length=10)