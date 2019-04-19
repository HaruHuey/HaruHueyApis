# 중간 처리
import datetime

from django.http import JsonResponse
from DatabasePy.models import *
from KakaoApi.WeatherIMG import WeatherIMG_DB
from DatabasePy.GoodCoin_Module.Coin_OutDataModule import module_re_co

Space = "\n"

def NoneReturnData():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "다시 시도해주세요."
        }
    })

# 오늘 급식
def Today_Meal():
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    QuerySet = str(MealData_Neis.objects.values(WeekModel[int(DB_Week)]).last()[WeekModel[int(DB_Week)]]).strip()

    return JsonResponse({
        "version": "2.0",
        "data": {
            "Date": Date,
            "Meal": QuerySet
        }
    })

# 내일 급식
def Tommorow_Meal():
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    if int(DB_Week) + 1 == 8:
        QuerySet = str(MealData_Neis.objects.values(WeekModel[int(1)]).last()[WeekModel[int(1)]])
        QuerySet = QuerySet.strip()
    else:
        QuerySet = str(MealData_Neis.objects.values(WeekModel[int(DB_Week + 1)]).last()[WeekModel[int(DB_Week + 1)]])
        QuerySet = QuerySet.strip()

    return JsonResponse({
        "version": "2.0",
        "data": {
            "Date": Date,
            "Meal": QuerySet
        }
    })

# 현재 날씨
def Weather_Now():
    QuerySet = Weather_skplanet.objects.last()
    wind_wspd = QuerySet.wind_wspd
    sky_name = QuerySet.sky_name
    temperature_tc = QuerySet.temperature_tc
    temperature_tmax = QuerySet.temperature_tmax
    temperature_tmin = QuerySet.temperature_tmin
    humidity = QuerySet.humidity

    # snowrain_type == 0:현상없음, 1:비, 2:비/눈, 3:눈
    snowrain_type = QuerySet.snowrain_type
    # snowrain_sinceOntime == if type=0/1/2 --> 강우량(mm) / if type=3 --> 적설량(cm)
    snowrain_sinceOntime = QuerySet.snowrain_sinceOntime
    # rain_sinceMidnight == if type=0/1/2 로 들어 올 경우 활성화
    rain_sinceMidnight = QuerySet.rain_sinceMidnight

    if snowrain_type == '0':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            'title': "현재 학교 주변 날씨",
                            'description': "현재 풍속 - " + wind_wspd + " m/s" + Space +
                                           "날씨 상태 - " + sky_name + Space +
                                           "현재 온도 - " + temperature_tc + "℃" + Space +
                                           "최고 기온 - " + temperature_tmax + "℃" + Space +
                                           "최저 기온 - " + temperature_tmin + "℃" + Space +
                                           "현재 습도 - " + humidity + "%",
                            'thumbnail': {
                                "imageUrl": WeatherIMG_DB(sky_name)
                            },
                            "buttons": [
                                {
                                    "label": "처음으로",
                                    "action": "block",
                                    "messageText": "처음으로"
                                },
                                {
                                    "label": "뒤로가기",
                                    "action": "block",
                                    "messageText": "날씨"
                                }
                            ]
                        }
                    }
                ]
            }
        })

    elif snowrain_type == '1' or snowrain_type == '2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            'title': "현재 학교 주변 날씨",
                            'description': "현재 풍속 - " + wind_wspd + " m/s" + Space +
                                           "날씨 상태 - " + sky_name + Space +
                                           "강수량(1시간) - " + snowrain_sinceOntime + "mm" + Space +
                                           "일일 강수량 - " + rain_sinceMidnight + "mm" + Space +
                                           "현재 온도 - " + temperature_tc + "℃" + Space +
                                           "최고 기온 - " + temperature_tmax + "℃" + Space +
                                           "최저 기온 - " + temperature_tmin + "℃" + Space +
                                           "현재 습도 - " + humidity + "%",
                            'thumbnail': {
                                "imageUrl": WeatherIMG_DB(sky_name)
                            },
                            "buttons": [
                                {
                                    "label": "처음으로",
                                    "action": "block",
                                    "messageText": "처음으로"
                                },
                                {
                                    "label": "뒤로가기",
                                    "action": "block",
                                    "messageText": "날씨"
                                }
                            ]
                        }
                    }
                ]
            }
        })

    elif snowrain_type == '3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            'title': "현재 학교 주변 날씨",
                            'description': "현재 풍속 - " + wind_wspd + " m/s" + Space +
                                           "날씨 상태 - " + sky_name + Space +
                                           "강우량(1시간) - " + snowrain_sinceOntime + "cm" + Space +
                                           "현재 온도 - " + temperature_tc + "℃" + Space +
                                           "최고 기온 - " + temperature_tmax + "℃" + Space +
                                           "최저 기온 - " + temperature_tmin + "℃" + Space +
                                           "현재 습도 - " + humidity + "%",
                            'thumbnail': {
                                "imageUrl": WeatherIMG_DB(sky_name)
                            },
                            "buttons": [
                                {
                                    "label": "처음으로",
                                    "action": "block",
                                    "messageText": "처음으로"
                                },
                                {
                                    "label": "뒤로가기",
                                    "action": "block",
                                    "messageText": "날씨"
                                }
                            ]
                        }
                    }
                ]
            }
        })

# 생활기상정보
# 미사용
def LifeIndex():
    QuerySet = Living_index.objects.last()

    fsnLife =  QuerySet.fsnLife
    Senso_temLife = QuerySet.Senso_temLife
    HeatLife = QuerySet.HeatLife
    DsplsLife = QuerySet.DsplsLife
    UltrvLife = QuerySet.UltrvLife
    WinterLife = QuerySet.WinterLife
    AirpllutionLife = QuerySet.AirpllutionLife
    Senso_HeatLife = QuerySet.Senso_HeatLife

    pass

# 보건기상정보
# 미사용
def HealthIndex():
    pass

# 대기 품질
def AirData_Total():
    QuerySet = AirData_airkorea.objects.last()

    Air_PM10 = QuerySet.Air_PM10
    Air_PM10_Context = QuerySet.Air_PM10_Context

    Air_PM25 = QuerySet.Air_PM25
    Air_PM25_Context = QuerySet.Air_PM25_Context

    Air_So2 = QuerySet.Air_So2
    Air_So2_Context = QuerySet.Air_So2_Context

    Air_No2 = QuerySet.Air_No2
    Air_No2_Context = QuerySet.Air_No2_Context

    Air_Co = QuerySet.Air_Co
    Air_Co_Context = QuerySet.Air_Co_Context

    Air_O3 = QuerySet.Air_O3
    Air_O3_Context = QuerySet.Air_O3_Context

    Air_Khai = QuerySet.Air_Khai
    Air_Khai_Context = QuerySet.Air_Khai_Context

    Context_AirData = "현재 학교 주변 대기품질입니다."

    Context_AirKorea = "API 제공 - 에어코리아\n" \
                       "데이터는 실시간 관측된 자료이며 측정소 현지 사정이나 데이터의 수신상태에 따라 미수신될 수 있습니다."

    return JsonResponse({
            "version": "2.0",
            "data": {
                "Data": Context_AirData + Space +
                        Air_Khai_Context + Space + "통합대기환경지수 ┃ " + Air_Khai + " ILO" + Space + Space +
                        "미세먼지 ┃ " + Air_PM10 + "㎍/㎥" + " '" + Air_PM10_Context + "'" + Space +
                        "초미세먼지 ┃ " + Air_PM25 + "㎍/㎥" + " '" + Air_PM25_Context + "'" + Space +
                        "아황산가스 ┃ " + Air_So2 + "ppm" + " '" + Air_So2_Context + "'" + Space +
                        "이산화질소 ┃ " + Air_No2 + "ppm" + " '" + Air_No2_Context + "'" + Space +
                        "일산화탄소 ┃ " + Air_Co + "ppm" + " '" + Air_Co_Context + "'" + Space +
                        "오존 ┃ " + Air_O3 + "ppm" + " '" + Air_O3_Context + "'" + Space +
                        Space + Context_AirKorea
            }
        })

# 미세먼지
def Air_Mise():
    QuerySet = AirData_airkorea.objects.last()

    Air_PM10 = QuerySet.Air_PM10
    Air_PM10_Context = QuerySet.Air_PM10_Context

    Air_PM25 = QuerySet.Air_PM25
    Air_PM25_Context = QuerySet.Air_PM25_Context

    Air_Khai = QuerySet.Air_Khai
    Air_Khai_Context = QuerySet.Air_Khai_Context

    Context_AirData = "현재 학교 주변 대기품질입니다."

    Context_AirKorea = "API 제공 - 에어코리아\n" \
                       "데이터는 실시간 관측된 자료이며 측정소 현지 사정이나 데이터의 수신상태에 따라 미수신될 수 있습니다."

    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": Context_AirData + Space +
                    Air_Khai_Context + Space + "통합대기환경지수 ┃ " + Air_Khai + " ILO" + Space + Space +
                    "미세먼지 ┃ " + Air_PM10 + "㎍/㎥" + " '" + Air_PM10_Context + "'" + Space +
                    "초미세먼지 ┃ " + Air_PM25 + "㎍/㎥" + " '" + Air_PM25_Context + "'" + Space +
                    Space + Context_AirKorea
        }
    })

# 미세먼지 예보
def Air_Mise_forecast():
    QuerySet = AirData_airkorea_forecast.objects.last()

    Air_PM10_forecast = QuerySet.Air_PM10_forecast
    Air_PM10_forecast_Context = QuerySet.Air_PM10_forecast_Context

    Air_PM25_forecast = QuerySet.Air_PM25_forecast
    Air_PM25_forecast_Context = QuerySet.Air_PM25_forecast_Context

    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "미세먼지 ┃ " + Air_PM10_forecast + "㎍/㎥" + " '" + Air_PM10_forecast_Context + "'" + Space +
                    "초미세먼지 ┃ " + Air_PM25_forecast + "㎍/㎥" + " '" + Air_PM25_forecast_Context + "'"
        }
    })

# 칭찬코인
# 미사용
def GoodCoin(req_param):
    return JsonResponse({
        "version": "2.0",
        "data": {
            "name": 'name',
            "coin": 'coin'
        }
    })

# 대나무숲 문자형
# 미사용
def Bamboo_Forest_Text():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 대나무숲 이미지 + 문자형
# 미사용
def Bamboo_Forest_Image( ):
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 건의사항
# 미사용
def Suggestions():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 질문사항
# 미사용
def Questions():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 음악신청
# 미사용
def MusicApply():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 학교 정보
def School_Info():
    Context = "IT 특성화 고등학교" + Space + "서울아이티고등학교!" + Space + Space + \
              "학과 목록" + Space + "컴퓨터전기전자과" + Space + "네트워크보안솔루션과" + \
              Space + "스마트웹콘텐츠과" + Space + "폴리메카닉스과" + Space + \
              "학교 분류 ┃ 특성화고등학교" + Space + "관할 교육청 ┃ 서울특별시교육청" + Space + \
              "전화 번호 ┃ 02-948-1901"

    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": Context
        }
    })

# 컴퓨터전기전자과
def department_Computer():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 네트워크보안솔루션과
def department_Network():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 스마트웹콘텐츠과
def department_WebContent():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 폴리메카닉스과
def department_Poly():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 도제학급
def department_apprentice():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

# 상세주소
def SchoolAdress():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "서울특별시 노원구 섬밭로 299 (서울아이티고등학교)"
        }
    })

# 우편번호
def SchoolPost():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "01773"
        }
    })

# 개교기념일
def SchoolDay():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "1992년 10월 30일"
        }
    })

# 전화번호
def SchoolNumber():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "02-948-1901"
        }
    })

# 팩스번호
def SchoolFax():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "02-977-8269"
        }
    })

# 모듈 호출 예정 / 데일리 브리핑
def DailyTo():
    return JsonResponse({
        "version": "2.0",
        "data": {
            "Data": "준비중"
        }
    })

'''
# 칭찬코인
def GoodCoin(req_param):
    print(str("통과"))
    DataCoin = module_re_co(KeyData=req_param)
    print(str(DataCoin))
    return JsonResponse({
        "version": "2.0",
        "data": {
            "name": DataCoin['name'],
            "coin": DataCoin['coin']
        }
    })
'''