#-*- coding: utf-8 -*-
# 미세먼지 및 통합 대기질 정보 제공
# 새로운 API 사용
# 2018 . 07 . 09 @ 예외 처리 추가로 오류 보정
# 2018 . 07 . 09 @ 추가 모듈화 작업
# 2019 . 03 . 10 @ 코드 속도 개선 / 안정화 작업 / 데이터베이스 저장 추가
import datetime
import json
import urllib.request
import random
from bs4 import BeautifulSoup
from DatabasePy.models import AirData_airkorea, AirData_airkorea_forecast
import os

Ot_So2 = "데이터를 불러오지 못했습니다."
Ot_Co = "데이터를 불러오지 못했습니다."
Ot_O3 = "데이터를 불러오지 못했습니다."
Ot_No2 = "데이터를 불러오지 못했습니다."
Ot_PM10 = "데이터를 불러오지 못했습니다."
Ot_PM25 = "데이터를 불러오지 못했습니다."
Ot_Khai = "데이터를 불러오지 못했습니다."

def Api():
    BaseUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={{ CODE }}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={{ SERVICE_KEY }}&ver=1.3"
    Open_URL_Air = urllib.request.urlopen(BaseUrl, timeout=5).read().decode("utf-8")
    Bs4_Air_Data = BeautifulSoup(Open_URL_Air, "html.parser")
    Bs4_Air_Data = Bs4_Air_Data.findAll("item")
    Bs4_Air_Data = Bs4_Air_Data[0]

    try:
        DataTime = Bs4_Air_Data.datatime.string
    except:
        DataTime = "API Time Zero"

    try:
        So2 = float(Bs4_Air_Data.so2value.string)
    except:
        So2 = Bs4_Air_Data.so2value.string

    try:
        Co = float(Bs4_Air_Data.covalue.string)
    except:
        Co = Bs4_Air_Data.covalue.string

    try:
        O3 = float(Bs4_Air_Data.o3value.string)
    except:
        O3 = Bs4_Air_Data.o3value.string

    try:
        No2 = float(Bs4_Air_Data.no2value.string)
    except:
        No2 = Bs4_Air_Data.no2value.string

    try:
        PM10 = int(Bs4_Air_Data.pm10value.string)
    except:
        PM10 = Bs4_Air_Data.pm10value.string

    try:
        PM25 = int(Bs4_Air_Data.pm25value.string)
    except:
        PM25 = Bs4_Air_Data.pm25value.string

    try:
        Khai = int(Bs4_Air_Data.khaivalue.string)
    except:
        Khai = Bs4_Air_Data.khaivalue.string

    def Air_So2():
        try:
            if So2 >= 0 and So2 < 0.01:
                Ot_So2 = "쾌적"
                return Ot_So2
            elif So2 >= 0.01 and So2 < 0.02:
                Ot_So2 = "좋음"
                return Ot_So2
            elif So2 >= 0.02 and So2 < 0.035:
                Ot_So2 = "보통"
                return Ot_So2
            elif So2 >= 0.035 and So2 < 0.05:
                Ot_So2 = "나쁨"
                return Ot_So2
            elif So2 >= 0.05 and So2 < 0.1:
                Ot_So2 = "매우 나쁨"
                return Ot_So2
            elif So2 >= 0.1 and So2 < 1:
                Ot_So2 = "치명적"
                return Ot_So2
            elif So2 >= 1:
                Ot_So2 = "지정 기준치 초과"
                return Ot_So2
            else:
                Ot_So2 = "아황산가스 분석 오류"
                return Ot_So2
        except:
            Ot_So2 = "정보 없음"
            return Ot_So2

    def Air_Co():
        try:
            if Co >= 0 and Co < 1:
                Ot_Co = "쾌적"
                return Ot_Co
            elif Co >= 1 and Co < 2:
                Ot_Co = "좋음"
                return Ot_Co
            elif Co >= 2 and Co < 7:
                Ot_Co = "보통"
                return Ot_Co
            elif Co >= 7 and Co < 12:
                Ot_Co = "나쁨"
                return Ot_Co
            elif Co >= 12 and Co < 25:
                Ot_Co = "매우 나쁨"
                return Ot_Co
            elif Co >= 25 and Co < 50:
                Ot_Co = "치명적"
                return Ot_Co
            elif Co >= 50:
                Ot_Co = "지정 기준치 초과"
                return Ot_Co
            else:
                Ot_Co = "일산화탄소 분석 오류"
                return Ot_Co
        except:
            Ot_Co = "정보 없음"
            return Ot_Co

    def Air_O3():
        try:
            if O3 >= 0 and O3 < 0.015:
                Ot_O3 = "쾌적"
                return Ot_O3
            elif O3 >= 0.015 and O3 < 0.03:
                Ot_O3 = "좋음"
                return Ot_O3
            elif O3 >= 0.03 and O3 < 0.045:
                Ot_O3 = "보통"
                return Ot_O3
            elif O3 >= 0.045 and O3 < 0.1:
                Ot_O3 = "나쁨"
                return Ot_O3
            elif O3 >= 0.1 and O3 < 0.3:
                Ot_O3 = "매우 나쁨"
                return Ot_O3
            elif O3 >= 0.3 and O3 < 0.6:
                Ot_O3 = "치명적"
                return Ot_O3
            elif O3 >= 0.6:
                Ot_O3 = "지정 기준치 초과"
                return Ot_O3
            else:
                Ot_O3 = "오존 분석 오류"
                return Ot_O3
        except:
            Ot_O3 = "정보 없음"
            return Ot_O3

    def Air_No2():
        try:
            if No2 >= 0 and No2 < 0.02:
                Ot_No2 = "쾌적"
                return Ot_No2
            elif No2 >= 0.02 and No2 < 0.03:
                Ot_No2 = "좋음"
                return Ot_No2
            elif No2 >= 0.03 and No2 < 0.05:
                Ot_No2 = "보통"
                return Ot_No2
            elif No2 >= 0.05 and No2 < 0.1:
                Ot_No2 = "나쁨"
                return Ot_No2
            elif No2 >= 0.1 and No2 < 0.15:
                Ot_No2 = "매우 나쁨"
                return Ot_No2
            elif No2 >= 0.15 and No2 < 2:
                Ot_No2 = "치명적"
                return Ot_No2
            elif No2 >= 2:
                Ot_No2 = "지정 기준치 초과"
                return Ot_No2
            else:
                Ot_No2 = "이산화질소 분석 오류"
                return Ot_No2
        except:
            Ot_No2 = "정보 없음"
            return Ot_No2

    def Air_PM10():
        try:
            if PM10 >= 0 and PM10 < 13:
                Ot_PM10 = "최고!"
                return Ot_PM10
            elif PM10 >= 13 and PM10 < 25:
                Ot_PM10 = "좋음"
                return Ot_PM10
            elif PM10 >= 25 and PM10 < 35:
                Ot_PM10 = "양호"
                return Ot_PM10
            elif PM10 >= 35 and PM10 < 45:
                Ot_PM10 = "보통"
                return Ot_PM10
            elif PM10 >= 45 and PM10 < 70:
                Ot_PM10 = "나쁨"
                return Ot_PM10
            elif PM10 >= 70 and PM10 < 95:
                Ot_PM10 = "상당히 나쁨"
                return Ot_PM10
            elif PM10 >= 95 and PM10 < 125:
                Ot_PM10 = "매우 나쁨"
                return Ot_PM10
            elif PM10 >= 125 and PM10 < 160:
                Ot_PM10 = "최악"
                return Ot_PM10
            elif PM10 >= 160 and PM10 < 250:
                Ot_PM10 = "매우 치명적"
                return Ot_PM10
            elif PM10 >= 250 and PM10 < 600:
                Ot_PM10 = "* 매우 치명적 *"
                return Ot_PM10
            elif PM10 >= 600:
                Ot_PM10 = "지정 기준치 초과"
                return Ot_PM10
            else:
                Ot_PM10 = "미세먼지 ( PM 10 ) 분석 오류"
                return Ot_PM10
        except:
            Ot_PM10 = "정보 없음"
            return Ot_PM10

    def Air_PM25():
        try:
            if PM25 >= 0 and PM25 < 6:
                Ot_PM25 = "최고!"
                return Ot_PM25
            elif PM25 >= 6 and PM25 < 13:
                Ot_PM25 = "좋음"
                return Ot_PM25
            elif PM25 >= 13 and PM25 < 20:
                Ot_PM25 = "양호"
                return Ot_PM25
            elif PM25 >= 20 and PM25 < 25:
                Ot_PM25 = "보통"
                return Ot_PM25
            elif PM25 >= 25 and PM25 < 35:
                Ot_PM25 = "나쁨"
                return Ot_PM25
            elif PM25 >= 35 and PM25 < 45:
                Ot_PM25 = "상당히 나쁨"
                return Ot_PM25
            elif PM25 >= 45 and PM25 < 70:
                Ot_PM25 = "매우 나쁨"
                return Ot_PM25
            elif PM25 >= 70 and PM25 < 85:
                Ot_PM25 = "최악"
                return Ot_PM25
            elif PM25 >= 85 and PM25 < 95:
                Ot_PM25 = "매우 치명적"
                return Ot_PM25
            elif PM25 >= 95 and PM25 < 600:
                Ot_PM25 = "* 매우 치명적 *"
                return Ot_PM25
            elif PM25 >= 600:
                Ot_PM25 = "지정 기준치 초과"
                return Ot_PM25
            else:
                Ot_PM25 = "초미세먼지 ( PM 2.5 ) 분석 오류"
                return Ot_PM25
        except:
            Ot_PM25 = "정보 없음"
            return Ot_PM25

    def Air_Khai():
        try:
            if Khai >= 0 and Khai < 40:
                Ot_Khai = "현재 종합 대기 품질은 매우 쾌적합니다!", "현재 매우 쾌적한 대기입니다!", "오랫만에 맑은 공기를 느껴보세요!(웃음)", "밖에 나가기 좋은 공기! 매우 쾌적해요!"
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            elif Khai >= 40 and Khai < 80:
                Ot_Khai = "현재 종합 대기 품질은 양호합니다!", "현재 양호한 대기입니다.", "양호해도 마스크는 착용하는게 좋아요!!"
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            elif Khai >= 80 and Khai < 150:
                Ot_Khai = "현재 종합 대기 품질은 나쁨입니다.", "대기 상태는 나쁨입니다.", "나쁨이에요... 외출을 자제해주세요 ㅠㅠ", "외출을 꼭 해야된다면 PM2.5까지 막을 수 있는 마스크를 착용해주세요. 대기질 상태가 나쁨이에요."
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            elif Khai >= 150 and Khai < 200:
                Ot_Khai = "현재 종합 대기 품질은 매우 나쁨입니다.", "대기 상태는 매우 나쁨입니다.", "외부 활동을 하지 말아주세요...", "매우 나쁨! 외부 활동은 안되요!"
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            elif Khai >= 200 and Khai < 250:
                Ot_Khai = "현재 종합 대기 품질은 최악입니다.", "대기 상태는 최악입니다.", "외부 활동을 하지 말아주세요."
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            elif Khai >= 250:
                Ot_Khai = "현재 종합 대기 품질은 치명적입니다.", "대기 상태는 치명적입니다.", "외출 후에는 샤워를 해주세요.", "외출을 자제해주세요."
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
            else:
                Ot_Khai = "통합대기환경지수 분석 오류"
                Ot_Khai = random.choice(Ot_Khai)
                return Ot_Khai
        except:
            Ot_Khai = "정보 없음"
            return Ot_Khai

    return {'DataTime':DataTime, 'So2':str(So2), 'Air_So2':Air_So2(), 'No2':str(No2),
            'Air_No2':Air_No2(), 'Co':str(Co), 'Air_Co':Air_Co(), 'O3':str(O3), 'Air_O3':Air_O3(),
            'PM10':str(PM10), 'Air_PM10':Air_PM10(), 'PM25':str(PM25), 'Air_PM25':Air_PM25(),
            'Air_Khai':Air_Khai(), 'Khai':str(Khai)}

def airdata_total():
    DataTime_Context = Api()['DataTime'] + "\n"
    Air_So2_Context = "아황산 가스 ┃ " + Api()[str('So2')] + "ppm" + "' " + Api()['Air_So2'] + " '\n"
    Air_No2_Context = "이산화 질소 ┃ " + Api()[str('No2')] + "ppm" + "' " + Api()['Air_No2'] + " '\n"
    Air_Co_Context = "일산화 탄소 ┃ " + Api()[str('Co')] + "ppm" + "' " + Api()['Air_Co'] + " '\n"
    Air_O3_Context = "오존 ┃ " + Api()[str('O3')] + "ppm" + "' " + Api()['Air_O3'] + " '\n\n"
    Air_PM10_Context = "미세 먼지 ┃ " + Api()[str('PM10')] + "㎍/㎥" + "' " + Api()['Air_PM10'] + " '\n"
    Air_PM25_Context = "초미세 먼지 ┃ " + Api()[str('PM25')] + "㎍/㎥" + "' " + Api()['Air_PM25'] + " '\n"
    Air_Khai_Context = Api()['Air_Khai'] + "\n통합대기환경지수 ┃ " + Api()[str('Khai')] + " ILO\n\n"

    # "┏━━━━━━━━━━━━━━━━━━┓" + "\n\n"
    #   \n\n" +\ "┗━━━━━━━━━━━━━━━━━━┛"
    try:
        Context = Air_Khai_Context + DataTime_Context + Air_PM10_Context + Air_PM25_Context +\
                  Air_So2_Context + Air_No2_Context + Air_Co_Context + Air_O3_Context +\
                  "API 제공 ┃ 에어코리아(환경부)\n\n" +\
                  "데이터는 실시간 관측된 자료이며 측정소 현지 사정이나 데이터의 수신상태에 따라 미수신될 수 있습니다."
    except:
        Context = "상계 측정소 API 오류\n\n" + "API 제공 ┃ 에어코리아(환경부)\n" +\
                  "데이터는 실시간 관측된 자료이며 측정소 현지 사정이나 데이터의 수신상태에 따라 미수신될 수 있습니다."

    return Context

def airdata_total_en():
    BaseUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={{ CODE }}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={{ SERVICE_KEY }}&ver=1.3"
    Open_URL_Air = urllib.request.urlopen(BaseUrl, timeout=5).read().decode("utf-8")
    Bs4_Air_Data = BeautifulSoup(Open_URL_Air, "html.parser")
    Bs4_Air_Data = Bs4_Air_Data.findAll("item")
    Bs4_Air_Data = Bs4_Air_Data[0]

    DataTime = Bs4_Air_Data.datatime.string
    pm10_24 = Bs4_Air_Data.pm10value24.string
    pm25_24 = Bs4_Air_Data.pm25value24.string

    Context = "┏━━━━━━━━━━━━━┓" + "\n\n" + "    Fine dust 24 hour forecast menu\n" + "    Fine Dust(PM10) ┃ " + pm10_24 + "㎍/㎥\n" + \
              "    Ultrafine Dust(PM2.5) ┃ " + pm25_24 + "㎍/㎥\n\n" + "┗━━━━━━━━━━━━━┛"

    return Context

def airdata_count24():
    BaseUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={{ CODE }}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={{ SERVICE_KEY }}&ver=1.3"
    Open_URL_Air = urllib.request.urlopen(BaseUrl, timeout=5).read().decode("utf-8")
    Bs4_Air_Data = BeautifulSoup(Open_URL_Air, "html.parser")
    Bs4_Air_Data = Bs4_Air_Data.findAll("item")
    Bs4_Air_Data = Bs4_Air_Data[0]

    DataTime = Bs4_Air_Data.datatime.string
    pm10_24 = Bs4_Air_Data.pm10value24.string
    pm25_24 = Bs4_Air_Data.pm25value24.string

    Context = "┏━━━━━━━━━━━━━┓" + "\n\n" + "    미세먼지 24시간 예보 메뉴\n" + "    미세먼지 ┃ " + pm10_24 + "㎍/㎥\n" +\
              "    초미세먼지 ┃ " + pm25_24 + "㎍/㎥\n\n" + "┗━━━━━━━━━━━━━┛"

    return Context

def airdate_count24_To():
    BaseUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={{ CODE }}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={{ SERVICE_KEY }}&ver=1.3"
    Open_URL_Air = urllib.request.urlopen(BaseUrl, timeout=5).read().decode("utf-8")
    Bs4_Air_Data = BeautifulSoup(Open_URL_Air, "html.parser")
    Bs4_Air_Data = Bs4_Air_Data.findAll("item")
    Bs4_Air_Data = Bs4_Air_Data[0]

    try:
        PM10 = int(Bs4_Air_Data.pm10value.string)
    except:
        PM10 = int(Bs4_Air_Data.pm10value.string)

    try:
        PM25 = int(Bs4_Air_Data.pm25value.string)
    except:
        PM25 = int(Bs4_Air_Data.pm25value.string)

    def Air_PM10():
        try:
            if PM10 >= 0 and PM10 < 13:
                Ot_PM10 = "최고!"
                return Ot_PM10
            elif PM10 >= 13 and PM10 < 25:
                Ot_PM10 = "좋음"
                return Ot_PM10
            elif PM10 >= 25 and PM10 < 35:
                Ot_PM10 = "양호"
                return Ot_PM10
            elif PM10 >= 35 and PM10 < 45:
                Ot_PM10 = "보통"
                return Ot_PM10
            elif PM10 >= 45 and PM10 < 70:
                Ot_PM10 = "나쁨"
                return Ot_PM10
            elif PM10 >= 70 and PM10 < 95:
                Ot_PM10 = "상당히 나쁨"
                return Ot_PM10
            elif PM10 >= 95 and PM10 < 125:
                Ot_PM10 = "매우 나쁨"
                return Ot_PM10
            elif PM10 >= 125 and PM10 < 160:
                Ot_PM10 = "최악"
                return Ot_PM10
            elif PM10 >= 160 and PM10 < 250:
                Ot_PM10 = "매우 치명적"
                return Ot_PM10
            elif PM10 >= 250 and PM10 < 600:
                Ot_PM10 = "* 매우 치명적 *"
                return Ot_PM10
            elif PM10 >= 600:
                Ot_PM10 = "지정 기준치 초과"
                return Ot_PM10
            else:
                Ot_PM10 = "미세먼지 ( PM 10 ) 분석 오류"
                return Ot_PM10
        except:
            Ot_PM10 = "정보 없음"
            return Ot_PM10

    def Air_PM25():
        try:
            if PM25 >= 0 and PM25 < 6:
                Ot_PM25 = "최고!"
                return Ot_PM25
            elif PM25 >= 6 and PM25 < 13:
                Ot_PM25 = "좋음"
                return Ot_PM25
            elif PM25 >= 13 and PM25 < 20:
                Ot_PM25 = "양호"
                return Ot_PM25
            elif PM25 >= 20 and PM25 < 25:
                Ot_PM25 = "보통"
                return Ot_PM25
            elif PM25 >= 25 and PM25 < 35:
                Ot_PM25 = "나쁨"
                return Ot_PM25
            elif PM25 >= 35 and PM25 < 45:
                Ot_PM25 = "상당히 나쁨"
                return Ot_PM25
            elif PM25 >= 45 and PM25 < 70:
                Ot_PM25 = "매우 나쁨"
                return Ot_PM25
            elif PM25 >= 70 and PM25 < 85:
                Ot_PM25 = "최악"
                return Ot_PM25
            elif PM25 >= 85 and PM25 < 95:
                Ot_PM25 = "매우 치명적"
                return Ot_PM25
            elif PM25 >= 95 and PM25 < 600:
                Ot_PM25 = "* 매우 치명적 *"
                return Ot_PM25
            elif PM25 >= 600:
                Ot_PM25 = "지정 기준치 초과"
                return Ot_PM25
            else:
                Ot_PM25 = "초미세먼지 ( PM 2.5 ) 분석 오류"
                return Ot_PM25
        except:
            Ot_PM25 = "정보 없음"
            return Ot_PM25

    def To_Co(To_AirCo):
        To = open('KakaoApi/To_Air_Context_' + To_AirCo + '.txt', 'r', encoding='UTF8')
        To_list = To.readlines()
        count_To = To_list[
            random.randint(1, sum(1 for line in open('KakaoApi/To_Air_Context_' + To_AirCo + '.txt', 'r', encoding='UTF8')) - 1)].rstrip('\r|\n')
        To.close()
        return count_To

    def Air_Context():
        try:
            if Air_PM10() in ["최고!", "좋음"] or Air_PM25() in ["최고!", "좋음"]:
                To_AirCo = "Good"
                return To_Co(To_AirCo)
            elif Air_PM10() in ["양호", "보통"] or Air_PM25() in ["양호", "보통"]:
                To_AirCo = "Soso"
                return To_Co(To_AirCo)
            elif Air_PM10() in ["나쁨", "상당히 나쁨"] or Air_PM25() in ["나쁨", "상당히 나쁨"]:
                To_AirCo = "SoB"
                return To_Co(To_AirCo)
            elif Air_PM10() in ["매우 나쁨", "최악"] or Air_PM25() in ["매우 나쁨", "최악"]:
                To_AirCo = "SadAir"
                return To_Co(To_AirCo)
            elif Air_PM10() in ["매우 치명적", "* 매우 치명적 *"] or Air_PM25() in ["매우 치명적", "* 매우 치명적 *"]:
                To_AirCo = "ExWa"
                return To_Co(To_AirCo)
            else:
                return "대기품질 데이터에 대한 Context 가 없습니다 ㅠ_ㅠ..."
        except:
            return "R - 대기품질 데이터에 대한 Context 가 없습니다 ㅠ_ㅠ..."

    Context = Air_Context() + "\n" +\
              "미세먼지 ┃ " + str(PM10) + "㎍/㎥ " + "'" + Air_PM10() + "'\n" +\
              "초미세먼지 ┃ " + str(PM25) + "㎍/㎥ " + "'" + Air_PM25() + "'"

    return Context

def airdata_count24_api():
    BaseUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={{ CODE }}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={{ SERVICE_KEY }}&ver=1.3"
    Open_URL_Air = urllib.request.urlopen(BaseUrl, timeout=5).read().decode("utf-8")
    Bs4_Air_Data = BeautifulSoup(Open_URL_Air, "html.parser")
    Bs4_Air_Data = Bs4_Air_Data.findAll("item")
    Bs4_Air_Data = Bs4_Air_Data[0]

    # 수정 필요
    try:
        PM10 = int(Bs4_Air_Data.pm10value.string)
    except:
        PM10 = int(Bs4_Air_Data.pm10value.string)

    try:
        PM25 = int(Bs4_Air_Data.pm25value.string)
    except:
        PM25 = int(Bs4_Air_Data.pm25value.string)

    def Air_PM10():
        try:
            if PM10 >= 0 and PM10 < 13:
                Ot_PM10 = "최고!"
                return Ot_PM10
            elif PM10 >= 13 and PM10 < 25:
                Ot_PM10 = "좋음"
                return Ot_PM10
            elif PM10 >= 25 and PM10 < 35:
                Ot_PM10 = "양호"
                return Ot_PM10
            elif PM10 >= 35 and PM10 < 45:
                Ot_PM10 = "보통"
                return Ot_PM10
            elif PM10 >= 45 and PM10 < 70:
                Ot_PM10 = "나쁨"
                return Ot_PM10
            elif PM10 >= 70 and PM10 < 95:
                Ot_PM10 = "상당히 나쁨"
                return Ot_PM10
            elif PM10 >= 95 and PM10 < 125:
                Ot_PM10 = "매우 나쁨"
                return Ot_PM10
            elif PM10 >= 125 and PM10 < 160:
                Ot_PM10 = "최악"
                return Ot_PM10
            elif PM10 >= 160 and PM10 < 250:
                Ot_PM10 = "매우 치명적"
                return Ot_PM10
            elif PM10 >= 250 and PM10 < 600:
                Ot_PM10 = "* 매우 치명적 *"
                return Ot_PM10
            elif PM10 >= 600:
                Ot_PM10 = "지정 기준치 초과"
                return Ot_PM10
            else:
                Ot_PM10 = "미세먼지 ( PM 10 ) 분석 오류"
                return Ot_PM10
        except:
            Ot_PM10 = "정보 없음"
            return Ot_PM10

    def Air_PM25():
        try:
            if PM25 >= 0 and PM25 < 6:
                Ot_PM25 = "최고!"
                return Ot_PM25
            elif PM25 >= 6 and PM25 < 13:
                Ot_PM25 = "좋음"
                return Ot_PM25
            elif PM25 >= 13 and PM25 < 20:
                Ot_PM25 = "양호"
                return Ot_PM25
            elif PM25 >= 20 and PM25 < 25:
                Ot_PM25 = "보통"
                return Ot_PM25
            elif PM25 >= 25 and PM25 < 35:
                Ot_PM25 = "나쁨"
                return Ot_PM25
            elif PM25 >= 35 and PM25 < 45:
                Ot_PM25 = "상당히 나쁨"
                return Ot_PM25
            elif PM25 >= 45 and PM25 < 70:
                Ot_PM25 = "매우 나쁨"
                return Ot_PM25
            elif PM25 >= 70 and PM25 < 85:
                Ot_PM25 = "최악"
                return Ot_PM25
            elif PM25 >= 85 and PM25 < 95:
                Ot_PM25 = "매우 치명적"
                return Ot_PM25
            elif PM25 >= 95 and PM25 < 600:
                Ot_PM25 = "* 매우 치명적 *"
                return Ot_PM25
            elif PM25 >= 600:
                Ot_PM25 = "지정 기준치 초과"
                return Ot_PM25
            else:
                Ot_PM25 = "초미세먼지 ( PM 2.5 ) 분석 오류"
                return Ot_PM25
        except:
            Ot_PM25 = "정보 없음"
            return Ot_PM25

    return {"PM10": PM10, "PM25": PM25, "Air_PM10": Air_PM10(), "Air_PM25": Air_PM25()}

def AirData_Database_in():
    Api_Call = Api()

    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    Air_So2 = Api_Call[str('So2')]
    Air_Co = Api_Call[str('Co')]
    Air_O3 = Api_Call[str('O3')]
    Air_No2 = Api_Call[str('No2')]
    Air_PM10 = Api_Call[str('PM10')]
    Air_PM25 = Api_Call[str('PM25')]
    Air_Khai = Api_Call[str('Khai')]

    Air_So2_Context = Api_Call["Air_So2"]
    Air_Co_Context = Api_Call["Air_Co"]
    Air_O3_Context = Api_Call["Air_O3"]
    Air_No2_Context = Api_Call["Air_No2"]
    Air_PM10_Context = Api_Call["Air_PM10"]
    Air_PM25_Context = Api_Call["Air_PM25"]
    Air_Khai_Context = Api_Call["Air_Khai"]

    AirData_airkorea.objects.create(DateTime=DateTime, Air_So2=Air_So2, Air_So2_Context=Air_So2_Context,
                                    Air_Co=Air_Co, Air_Co_Context=Air_Co_Context, Air_O3=Air_O3,
                                    Air_O3_Context=Air_O3_Context, Air_No2=Air_No2, Air_No2_Context=Air_No2_Context,
                                    Air_PM10=Air_PM10, Air_PM10_Context=Air_PM10_Context,
                                    Air_PM25=Air_PM25, Air_PM25_Context=Air_PM25_Context,
                                    Air_Khai=Air_Khai, Air_Khai_Context=Air_Khai_Context)

    return "저장 완료"

def AirData_forecast_DB_in():
    Api_Call = airdata_count24_api()

    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    Air_PM10 = Api_Call[str("PM10")]
    Air_PM25 = Api_Call[str("PM25")]

    Air_PM10_Context = Api_Call["Air_PM10"]
    Air_PM25_Context = Api_Call["Air_PM25"]

    AirData_airkorea_forecast.objects.create(DateTime=DateTime, Air_PM10_forecast=Air_PM10, Air_PM10_forecast_Context=Air_PM10_Context,
                                             Air_PM25_forecast=Air_PM25, Air_PM25_forecast_Context=Air_PM25_Context)

    return "저장 완료"

def API_Call_AirData():
    try:
        AirData_Database_in()
        AirData_forecast_DB_in()
    except:
        pass
    return "저장 완료"