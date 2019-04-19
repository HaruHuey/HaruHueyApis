import datetime
import json
from pprint import pprint
import urllib.request
from DatabasePy.models import Health_index

# 공식 API문서 잘못 작성 된 부분 보고
# 기상청 주무관님이 DATA.GO.KR에 수정 반영 요청 후 반영 됨

# 단계 및 범위
# 낮음 - 0
# 보통 - 1
# 높음 - 2
# 매우높음 - 3

# 데이터 갱신(생산) 06시, 18시
# 오전 6시 5분과 오후 6시 5분에 데이터 갱신
# 오후 6시 이후 데이터는 당일 데이터가 없으므로 기존 데이터 이용
# 6시 이후에는 06 Key 데이터 조회
# 18시 이후에는 18 Key 데이터 조회 + 06 Key 데이터 조회

# 월 가져오기
def time_m():
    time_con = datetime.datetime.now().strftime('%m')
    time_dt = int(time_con)
    return time_dt

def Health_index_Data():
    time_con = datetime.datetime.now().strftime('%m')
    time_dt = int(time_con)

    TimeData = str(datetime.datetime.now().strftime("%Y%m%d%H"))
    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    H_time = int(datetime.datetime.now().strftime('%H'))

    # 감기 가능 지수 / 9월 ~ 4월
    def inflWho():
        if time_dt in [9, 10, 11, 12, 1, 2, 3, 4]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getInflWhoList?areaNo=1135062500&ServiceKey="
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

    # 천식 · 폐질환 가능 지수 / 연중 제공
    def AsthmaWho():
        try:
            URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getAsthmaWhoList?areaNo=1135062500&ServiceKey="
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

    # 뇌졸중 가능 지수 / 연중 제공
    def BrainWho():
        try:
            URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getBrainWhoList?areaNo=1135062500&ServiceKey="
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

    # 피부 질환 가능 지수 / 연중 제공
    def SkinWho():
        try:
            URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getSkinWhoList?areaNo=1135062500&ServiceKey="
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

    # 꽃가루 농도 위험 지수 ( 참나무 ) / 4월 ~ 5월
    def FlowerWoodyWho():
        if time_dt in [4, 5]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getFlowerWoodyWhoList?areaNo=1135062500&ServiceKey="
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

    # 꽃가루 농도 위험 지수 ( 소나무 ) / 4월 ~ 5월
    def FlowerPineWho():
        if time_dt in [4, 5]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getFlowerPineWhoList?areaNo=1135062500&ServiceKey="
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

    # 꽃가루 농도 위험 지수 ( 잡초류 ) / 9월 ~ 10월
    def FlowerWeedsWho():
        if time_dt in [9, 10]:
            try:
                URL = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getFlowerWeedsWhoList?areaNo=1135062500&ServiceKey="
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

    if H_time in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        # 추가 / 오늘
        Health_index.objects.create(DateTime=DateTime, inflWho=inflWho()["today"], AsthmaWho=AsthmaWho()["today"],
                                    BrainWho=BrainWho()["today"], SkinWho=SkinWho()["today"],
                                    FlowerWoodyWho=FlowerWoodyWho()["today"],
                                    FlowerPineWho=FlowerPineWho()["today"], FlowerWeedsWho=FlowerWeedsWho()["today"])

    elif H_time in [20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6]:
        # 업데이트 / 내일
        Health_index.objects.update(DateTime=DateTime, inflWho=inflWho()["tomorrow"], AsthmaWho=AsthmaWho()["tomorrow"],
                                    BrainWho=BrainWho()["tomorrow"], SkinWho=SkinWho()["tomorrow"],
                                    FlowerWoodyWho=FlowerWoodyWho()["tomorrow"],
                                    FlowerPineWho=FlowerPineWho()["tomorrow"], FlowerWeedsWho=FlowerWeedsWho()["tomorrow"])
        pass
    else:
        # 추가 / 오늘
        Health_index.objects.create(DateTime=DateTime, inflWho=inflWho()["today"], AsthmaWho=AsthmaWho()["today"],
                                    BrainWho=BrainWho()["today"], SkinWho=SkinWho()["today"],
                                    FlowerWoodyWho=FlowerWoodyWho()["today"],
                                    FlowerPineWho=FlowerPineWho()["today"], FlowerWeedsWho=FlowerWeedsWho()["today"])
        pass


    return "저장 완료"