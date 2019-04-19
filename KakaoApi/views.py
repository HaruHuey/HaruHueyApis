import json
import re
from pprint import pprint

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from KakaoApi.APIdataLogging import APIdataLogging
from KakaoApi.serializer import *

# Kakao Oauth 관리
@csrf_exempt
def oauth_kakao(request):
    code = str(request.args.get('code'))
    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=authorization_code&client_id=1e905007eaa1ccf2917524e847419aa4&redirect_uri=http://{{ URL }}/KakaoApi/oauth&code=" + str(code)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    access_token = json.loads(((response.text).encode('utf-8')))['access_token']

    url = "https://kapi.kakao.com/v1/user/signup"
    headers.update({'Authorization' : "Bearer" + str(access_token)})
    response = requests.request("POST", url, headers=headers)

    url = "https://kapi.kakao.com/v1/user/me"
    response = requests.request("POST", url, headers=headers)

    return (response.text)

# 칭찬코인 조회
# 미사용
# 10101 형식
@csrf_exempt
def KakaoApi_GoodCoin_First(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    pprint(LoadJson_req)
    return JsonResponse({
        "version": "2.0",
        "data": {
            "T": "Test"
        }
    })

# 급식
@csrf_exempt
def Meal(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "Date_Meal_Today" in detailParams or "오늘 급식" in intentName:
        return Today_Meal()

    elif "Date_Meal_HaruTo" in detailParams or "내일 급식" in intentName:
        return Tommorow_Meal()

    else:
        return NoneReturnData()

# 날씨
@csrf_exempt
def Weather(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "Weather" in detailParams or "현재 날씨" in intentName:
        return Weather_Now()

    else:
        return NoneReturnData()

# 대기 품질
@csrf_exempt
def AirData(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "AirData" in detailParams or "종합대기" in intentName:
        return AirData_Total()

    else:
        return NoneReturnData()

# 미세먼지
@csrf_exempt
def AirMise(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "AirData" in detailParams or "미세먼지" in intentName:
        return Air_Mise()

    else:
        return NoneReturnData()

# 미세먼지 에보
@csrf_exempt
def AirMise_forecast(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "AirData" in detailParams or "미세먼지 예보" in intentName:
        return Air_Mise_forecast()

    else:
        return NoneReturnData()

# 학교 정보
@csrf_exempt
def SchoolInfo(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "입학 정보" in intentName:
        return School_Info()

    else:
        return NoneReturnData()

# 학과 정보
@csrf_exempt
def DepartmentInfo(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "컴퓨터전기전자과" in intentName:
        return department_Computer()

    elif "네트워크보안솔루션과" in intentName:
        return department_Network()

    elif "스마트웹콘텐츠과" in intentName:
        return department_WebContent()

    elif "폴리메카닉스과" in intentName:
        return department_Poly()

    elif "도제학교" in intentName:
        return department_apprentice()

    else:
        return NoneReturnData()

# 학교 통합
@csrf_exempt
def SchoolData(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    intentName = str(LoadJson_req['intent']['name'])
    APIdataLogging(LoadJson_req)

    if "상세주소-도로명" in intentName:
        return SchoolAdress()

    elif "우편번호" in intentName:
        return SchoolPost()

    elif "개교기념일" in intentName:
        return SchoolDay()

    elif "전화번호" in intentName:
        return SchoolNumber()

    elif "팩스번호" in intentName:
        return SchoolFax()

    else:
        return NoneReturnData()
'''
# 칭찬코인
@csrf_exempt
def GoodCoin_API(request):
    OpenJson_req = ((request.body).decode('utf-8'))
    LoadJson_req = json.loads(OpenJson_req)
    detailParams = str(LoadJson_req['action']['params'])
    intentName = str(LoadJson_req['intent']['name'])
    req_param = LoadJson_req['action']['detailParams']['sys_number']['origin']
    print(req_param)
    APIdataLogging(LoadJson_req)

    if "sys_number" in detailParams or "칭찬코인" in intentName:
        print(req_param + detailParams)
        return GoodCoin(req_param=req_param)

    else:
        return NoneReturnData()
'''