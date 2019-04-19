# 중간 처리
import datetime

from django.http import JsonResponse
from DatabasePy.models import *

Space = "\n"
Help_return_apiflow = "서울아이티고등학교 리린 챗봇의 가이드입니다." + Space + Space + \
                      "1) 급식 조회 - 예)오늘 급식 뭐야?" + Space + \
                      "2) 칭찬코인 조회 - 예)1학년 1반 1번 칭찬코인 알려줘" + Space + \
                      "3) 대기품질 - 예)오늘 학교 주변 미세먼지 어때?" + Space + \
                      "4) 날씨 - 예)오늘 날씨 어때?" + Space + \
                      "5) 문의 하기 - 준비중" + Space + Space + \
                      "더 많은 기능과 개선 작업을 진행 할 예정입니다! 문의 및 오류 제보 등은 https://open.kakao.com/o/saRSB9K 이 곳으로 보내주세요!"

Help_return_apiflow_en = "Seoul IT High School Ririn Chatbot's Guide." + Space + Space + \
                         "1) Cafeteria Lookup - Ex)Today Meal, Cafeteria" + Space + \
                         "2) Air Lookup - Ex)Air, AirData, Fine Dust" + Space + \
                         "3) Weather - Ex)Weather" + Space + \
                         "More features and improvements are planned! Please send inquiries and error reports to https://open.kakao.com/o/saRSB9K Here!"

HaruIN_return_apiflow = "안녕하세요! 서울아이티고등학교 리린입니다. 무엇을 도와드릴까요?"

HaruIN_return_apiflow_en = "Hi! Seoul IT High School Ririn. How can I help you?"

def returnData():
    return JsonResponse({
        "fulfillmentText": "None Context"
    })

# 영어
# 시작
def en_IN_Intent():
    return JsonResponse({
        "fulfillmentText": HaruIN_return_apiflow_en
    })

# 급식 - 오늘
def en_Meal_Today():
    # MealData_Neis_en.objects.last().Data
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    QuerySet = str(MealData_Neis_en.objects.values(WeekModel[int(DB_Week)]).last()[WeekModel[int(DB_Week)]]).strip()

    return JsonResponse({
        "fulfillmentText": Date + ' Today Cafeteria Menu' + Space + QuerySet
    })

# 급식 - 내일
def en_Meal_Tommorow():
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    QuerySet = str(MealData_Neis_en.objects.values(WeekModel[int(DB_Week + 1)]).last()[WeekModel[int(DB_Week + 1)]]).strip()

    return JsonResponse({
        "fulfillmentText": Date + ' Tommorow Cafeteria Menu' + Space + QuerySet
    })

# 대기환경정보
def en_AirData():
    QuerySet = AirData_airkorea.objects.last()
    Air_PM10DB = QuerySet.Air_PM10
    Air_PM25DB = QuerySet.Air_PM25
    return JsonResponse({
        "fulfillmentText": "Fine Dust(PM10) ┃ " + Air_PM10DB + '㎍/㎥' + Space + "Ultrafine Dust(PM2.5) ┃ " + Air_PM25DB + '㎍/㎥'
    })

# 도움말
def en_Help():
    return JsonResponse({
        "fulfillmentText": Help_return_apiflow_en
    })

# 날씨
def en_Weather():
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
            "fulfillmentText": "It's the Weather around School Now!" + Space +
                               "Wind Flow - " + wind_wspd + " m/s" + Space +
                               "Sky - " + sky_name + Space +
                               "Current temperature - " + temperature_tc + "℃" + Space +
                               "Highest temperature - " + temperature_tmax + "℃" + Space +
                               "Lowest temperature - " + temperature_tmin + "℃" + Space +
                               "Humidity - " + humidity + "%"
        })

    elif snowrain_type == '1' or snowrain_type == '2':
        return JsonResponse({
            "fulfillmentText": "It's the Weather around School Now!" + Space +
                               "Wind Flow - " + wind_wspd + " m/s" + Space +
                               "Sky - " + sky_name + Space +
                               "1 hour Rainfall - " + snowrain_sinceOntime + "mm" + Space +
                               "Cumulative precipitation" + rain_sinceMidnight + "mm" + Space +
                               "Current temperature - " + temperature_tc + "℃" + Space +
                               "Highest temperature - " + temperature_tmax + "℃" + Space +
                               "Lowest temperature - " + temperature_tmin + "℃" + Space +
                               "Humidity - " + humidity + "%"
        })

    elif snowrain_type == '3':
        return JsonResponse({
            "fulfillmentText": "It's the Weather around School Now!" + Space +
                               "Wind Flow - " + wind_wspd + " m/s" + Space +
                               "Sky - " + sky_name + Space +
                               "1 hour Snowfall - " + snowrain_sinceOntime + "cm" + Space +
                               "Current temperature - " + temperature_tc + "℃" + Space +
                               "Highest temperature - " + temperature_tmax + "℃" + Space +
                               "Lowest temperature - " + temperature_tmin + "℃" + Space +
                               "Humidity - " + humidity + "%"
        })



# None
def en_None():
    return JsonResponse({
        "fulfillmentText": returnData()
    })

# None Data
def en_NoneData():
    return JsonResponse({
        "fulfillmentText": returnData()
    })

# else
def en_else():
    return JsonResponse({
        "fulfillmentText": returnData()
    })

# 한국어
# 시작
def ko_IN_Intent():
    return JsonResponse({
        "fulfillmentText": Help_return_apiflow
    })

# 급식 - 오늘
def ko_Meal_Today():
    # MealData_Neis_en.objects.last().Data
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    QuerySet = str(MealData_Neis.objects.values(WeekModel[int(DB_Week)]).last()[WeekModel[int(DB_Week)]]).strip()

    return JsonResponse({
        "fulfillmentText": Date + ' 오늘 점심 메뉴에요.' + Space + QuerySet
    })

# 급식 - 내일
def ko_Meal_Tommorow():
    WeekModel = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    DB_Week = datetime.datetime.today().weekday()
    QuerySet = str(MealData_Neis.objects.values(WeekModel[int(DB_Week + 1)]).last()[WeekModel[int(DB_Week + 1)]]).strip()

    return JsonResponse({
        "fulfillmentText": Date + ' 다음날 점심 메뉴에요.' + Space + QuerySet
    })

# 대기환경정보
def ko_AirData():
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

    # ppm

    return JsonResponse({
        "fulfillmentText": Context_AirData + Space +
                           Air_Khai_Context + Space + "통합대기환경지수 ┃ " + Air_Khai + " ILO" + Space + Space +
                           "미세먼지 ┃ " + Air_PM10 + "㎍/㎥" + "' " + Air_PM10_Context + "'" + Space +
                           "초미세먼지 ┃ " + Air_PM25 + "㎍/㎥" + "' " + Air_PM25_Context + "'" + Space +
                           "아황산가스 ┃ " + Air_So2 + "ppm" + "' " + Air_So2_Context + "'" + Space +
                           "이산화질소 ┃ " + Air_No2 + "ppm" + "' " + Air_No2_Context + "'" + Space +
                           "일산화탄소 ┃ " + Air_Co + "ppm" + "' " + Air_Co_Context + "'" + Space +
                           "오존 ┃ " + Air_O3 + "ppm" + "' " + Air_O3_Context + "'" + Space +
                           Space + Context_AirKorea
    })

# 도움말
def ko_Help():
    return JsonResponse({
        "fulfillmentText": Help_return_apiflow
    })

# 날씨
def ko_Weather():
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
            "fulfillmentText": "현재 학교 주변 날씨입니다." + Space +
                               "현재 풍속 - " + wind_wspd + " m/s" + Space +
                               "날씨 상태 - " + sky_name + Space +
                               "현재 온도 - " + temperature_tc + "℃" + Space +
                               "최고 기온 - " + temperature_tmax + "℃" + Space +
                               "최저 기온 - " + temperature_tmin + "℃" + Space +
                               "현재 습도 - " + humidity + "%"
        })

    elif snowrain_type == '1' or snowrain_type == '2':
        return JsonResponse({
            "fulfillmentText": "현재 학교 주변 날씨입니다." + Space +
                               "현재 풍속 - " + wind_wspd + " m/s" + Space +
                               "날씨 상태 - " + sky_name + Space +
                               "강수량(1시간) - " + snowrain_sinceOntime + "mm" + Space +
                               "일일 강수량" + rain_sinceMidnight + "mm" + Space +
                               "현재 온도 - " + temperature_tc + "℃" + Space +
                               "최고 기온 - " + temperature_tmax + "℃" + Space +
                               "최저 기온 - " + temperature_tmin + "℃" + Space +
                               "현재 습도 - " + humidity + "%"
        })

    elif snowrain_type == '3':
        return JsonResponse({
            "fulfillmentText": "현재 학교 주변 날씨입니다." + Space +
                               "현재 풍속 - " + wind_wspd + " m/s" + Space +
                               "날씨 상태 - " + sky_name + Space +
                               "강수량(1시간) - " + snowrain_sinceOntime + "cm" + Space +
                               "현재 온도 - " + temperature_tc + "℃" + Space +
                               "최고 기온 - " + temperature_tmax + "℃" + Space +
                               "최저 기온 - " + temperature_tmin + "℃" + Space +
                               "현재 습도 - " + humidity + "%"
        })

# 칭찬코인 - Param
# 학교 코드 - S010000599
# 신규코드 개발 필요
def ko_GoodCoin_Param(First_param, Sec_param, Third_param):
    return JsonResponse({
        "fulfillmentText": "NONE"
    })

# 칭찬코인 - 문자인식
def ko_GoodCoin_Text(queryText_req):
    return JsonResponse({
        "fulfillmentText": "NONE"
    })

# 학교 정보
# 소개
def ko_SchoolContext():
    Context = "IT 특성화 고등학교" + Space + "서울아이티고등학교!" + Space + Space +\
              "학과 목록" + Space + "컴퓨터전기전자과" + Space + "네트워크보안솔루션과" +\
              Space + "스마트웹콘텐츠과" + Space + "폴리메카닉스과" + Space +\
              "학교 분류 ┃ 특성화고등학교" + Space + "관할 교육청 ┃ 서울특별시교육청" + Space +\
              "전화 번호 ┃ 02-948-1901"

    return JsonResponse({
        "fulfillmentText": Context
    })

# 상세주소
def ko_SchoolAdress():
    Context = "서울특별시 노원구 섬밭로 299 (서울아이티고등학교)"
    return JsonResponse({
        "fulfillmentText": Context
    })

# 우편번호
def ko_SchoolPost():
    Context = "01773"
    return JsonResponse({
        "fulfillmentText": Context
    })

# 개교기념일
def ko_SchoolDay():
    Context = "1992년 10월 30일"
    return JsonResponse({
        "fulfillmentText": Context
    })

# 전화번호
def ko_SchoolNumber():
    Context = "02-948-1901"
    return JsonResponse({
        "fulfillmentText": Context
    })

# 팩스번호
def ko_SchoolFax():
    Context = "02-977-8269"
    return JsonResponse({
        "fulfillmentText": Context
    })

# else
def ko_else():
    return JsonResponse({
        "fulfillmentText": "잠시 후에 다시 시도해주세요!"
    })


'''
def ko_GoodCoin_Param(First_param, Sec_param, Third_param):
    return JsonResponse({
        "fulfillmentText": ApiAi_re_co(First_param, Sec_param, Third_param)
    })

# 칭찬코인 - 문자인식
def ko_GoodCoin_Text(queryText_req):
    DataCoin = module_re_co(queryText_req)
    return JsonResponse({
        "fulfillmentText": DataCoin["name"] + " 학생의 칭찬코인은" + DataCoin["coin"] + " 개 입니다."
    })
'''