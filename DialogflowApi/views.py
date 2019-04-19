import json
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from DialogflowApi.models import *
from DialogflowApi.serializer import *

@csrf_exempt
def Apis_Views(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 개인 식별 ID
    responseId_req = LoadJson_req["responseId"]

    # 입력 된 값
    queryText_req = LoadJson_req["queryResult"]["queryText"]

    # 파라메터 정보 - 아래는 공통
    param_req = LoadJson_req["queryResult"]["parameters"]
    # 개별 DB 데이터 저장 및 분석

    # 언어 코드
    languageCode_req = LoadJson_req["queryResult"]["languageCode"]

    # 문장 의도 분석 값
    intent_displayName_req = LoadJson_req["queryResult"]["intent"]["displayName"]

    reqLog.objects.create(
        DateTime=DateTime,
        responseId_req=responseId_req,
        queryText_req=queryText_req,
        param_req=str(param_req),
        languageCode_req=languageCode_req,
        intent_displayName_req=intent_displayName_req
    )

    if "en" in languageCode_req:
        if "HaruIN" in param_req:
            return en_IN_Intent()

        elif "Meal" in param_req:
            if "Date_Meal_HaruTo" in param_req:
                return en_Meal_Tommorow()
            else:
                return en_Meal_Today()

        elif "AirData" in param_req:
            return en_AirData()

        elif "Help" in param_req:
            return en_Help()

        elif "Weather" in param_req:
            return en_Weather()

        elif "None" in param_req:
            return en_None()

        elif re.search('[$()a-zA-Z0-9]+', intent_displayName_req) or re.search('[$()a-zA-Z0-9]+', param_req):
            return en_NoneData()

        else:
            return en_else()

    elif "ko" in languageCode_req:
        if "HaruIN" in param_req:
            return ko_IN_Intent()

        elif "Meal" in param_req:
            if "Date_Meal_HaruTo" in param_req:
                return ko_Meal_Tommorow()
            else:
                return ko_Meal_Today()

        elif "AirData" in param_req:
            return ko_AirData()

        elif "Help" in param_req:
            return ko_Help()

        elif "Weather" in param_req:
            return ko_Weather()

        elif "GoodCoin" in param_req:
            if ("Coin_First_Param" and "Coin_Sec_Param" and "Coin_Third_Param") in param_req:
                First_param = param_req["Coin_First_Param"]
                Sec_param = param_req["Coin_Sec_Param"]
                Third_param = param_req["Coin_Third_Param"]

                return ko_GoodCoin_Param(First_param, Sec_param, Third_param)

            elif len(re.compile('[^0-9]+').sub('', queryText_req).rstrip('\r|\n')) == 5:
                return ko_GoodCoin_Text(queryText_req)

            else:
                return returnData()

        elif "School_Data" in param_req:
            School_Data_param_req = param_req["School_Data"]

            if School_Data_param_req == "학교 소개":
                return ko_SchoolContext()

            elif School_Data_param_req == "상세주소":
                return ko_SchoolAdress()

            elif School_Data_param_req == "우편번호":
                return ko_SchoolPost()

            elif School_Data_param_req == "개교기념일":
                return ko_SchoolDay()

            elif School_Data_param_req == "전화번호":
                return ko_SchoolNumber()

            elif School_Data_param_req == "팩스번호":
                return ko_SchoolFax()

            else:
                return ko_else()

        else:
            return returnData()

    else:
        return returnData()