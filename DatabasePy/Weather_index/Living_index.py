import datetime
import json
from DatabasePy.models import Living_index
from bs4 import BeautifulSoup
import urllib.request

# 월 가져오기
def time_m():
    time_con = datetime.datetime.now().strftime('%m')
    time_dt = int(time_con)
    return time_dt

def Living_index_Data():
    time_con = datetime.datetime.now().strftime('%m')
    time_dt = int(time_con)

    TimeData = str(datetime.datetime.now().strftime("%Y%m%d%H"))
    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    H_time = int(datetime.datetime.now().strftime('%H'))

    # 식중독 지수 / 연중 제공
    def fsnLife():
        try:
            URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getFsnLifeList?areaNo=1135062500&ServiceKey="
            ServiceKey = "{{ SERVICE_KEY }}"
            GET_KEY = "&time=" + TimeData + "&_type=" + "json"

            SET_URL = URL + ServiceKey + GET_KEY

            Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
            Read_URL = json.loads(Open_URL)

            JsonData = Read_URL["Response"]["body"]["indexModel"]
            todayData = str(JsonData["today"])
            tomorrowData = str(JsonData["tomorrow"])

            reqData = {"today":todayData, "tomorrow":tomorrowData}

            return reqData

        except:
            todayData = "정보 없음"
            tomorrowData = "정보 없음"

            reqData = {"today": todayData, "tomorrow": tomorrowData}

            return reqData

    # 체감 온도 / 11월 ~ 3월
    def Senso_temLife():
        if time_dt in [11, 12, 1, 2, 3]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getSensorytemLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 열 지수 / 6월 ~ 9월
    def HeatLife():
        if time_dt in [6, 7, 8, 9]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getHeatLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 불쾌 지수 / 6월 ~ 9월
    def DsplsLife():
        if time_dt in [6, 7, 8, 9]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getDsplsLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 자외선 지수 / 3월 ~ 11월 / 수정
    def UltrvLife():
        if time_dt in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getUltrvLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["today"])
                tomorrowData = str(JsonData["tomorrow"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 동파 가능 지수 / 12월 ~ 2월
    def WinterLife():
        if time_dt in [12, 1, 2]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getWinterLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 대기 확산 지수 / 11월 ~ 5월
    def AirpllutionLife():
        if time_dt in [11, 12, 1, 2, 3, 4, 5]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getAirpollutionLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData

    # 더위 체감 지수 / 5월 ~ 9월
    def Senso_HeatLife():
        if time_dt in [5, 6, 7, 8, 9]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getSensoryHeatLifeList?areaNo=1135062500&ServiceKey="
                ServiceKey = "{{ SERVICE_KEY }}"
                GET_KEY = "&time=" + TimeData + "&_type=" + "json"

                SET_URL = URL + ServiceKey + GET_KEY

                Open_URL = urllib.request.urlopen(SET_URL, timeout=10).read().decode("utf-8")
                Read_URL = json.loads(Open_URL)

                JsonData = Read_URL["Response"]["body"]["indexModel"]
                todayData = str(JsonData["h3"])
                tomorrowData = str(JsonData["h3"])

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData

            except:
                todayData = "정보 없음"
                tomorrowData = "정보 없음"

                reqData = {"today": todayData, "tomorrow": tomorrowData}

                return reqData
        else:
            todayData = "기간 아님"
            tomorrowData = "기간 아님"

            reqData = {"today": todayData, "tomorrow": tomorrowData}
            return reqData



    if H_time in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        # 추가 / 오늘
        Living_index.objects.create(DateTime=DateTime, fsnLife=fsnLife()["today"],
                                    Senso_temLife=Senso_temLife()["today"],
                                    HeatLife=HeatLife()["today"], DsplsLife=DsplsLife()["today"],
                                    UltrvLife=UltrvLife()["today"], WinterLife=WinterLife()["today"],
                                    AirpllutionLife=AirpllutionLife()["today"],
                                    Senso_HeatLife=Senso_HeatLife()["today"])

    elif H_time in [20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6]:
        # 업데이트 / 내일
        Living_index.objects.update(DateTime=DateTime, fsnLife=fsnLife()["tomorrow"],
                                    Senso_temLife=Senso_temLife()["tomorrow"],
                                    HeatLife=HeatLife()["tomorrow"], DsplsLife=DsplsLife()["tomorrow"],
                                    UltrvLife=UltrvLife()["tomorrow"], WinterLife=WinterLife()["tomorrow"],
                                    AirpllutionLife=AirpllutionLife()["tomorrow"],
                                    Senso_HeatLife=Senso_HeatLife()["tomorrow"])
    else:
        # 추가 / 오늘
        Living_index.objects.create(DateTime=DateTime, fsnLife=fsnLife()["today"],
                                    Senso_temLife=Senso_temLife()["today"],
                                    HeatLife=HeatLife()["today"], DsplsLife=DsplsLife()["today"],
                                    UltrvLife=UltrvLife()["today"], WinterLife=WinterLife()["today"],
                                    AirpllutionLife=AirpllutionLife()["today"],
                                    Senso_HeatLife=Senso_HeatLife()["today"])
        pass

    return "저장 완료"