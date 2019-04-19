import datetime
import json
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from DatabasePy.models import MealData_Neis, MealData_Neis_en
from DatabasePy.Trans_Papago import Trans


def MealData():
    # 급식이 담기는 공간 ( 비어있음 ) 월, 화, 수, 목, 금, 토, 일
    Pure_MealData = ['', '', '', '', '', '', '']
    Pure_MealData_en = ['', '', '', '', '', '', '']

    # 급식이 나와있는 홈페이지
    URL = "https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode={{ CODE }}&schulCrseScCode=4&schulKndScCode=4&schMmealScCode=2"

    # 홈페이지를 열고 읽어들인다
    Open_URL = urllib.request.urlopen(URL, timeout=5).read()

    # BeautifulSoup 을 사용해서 Html 파일을 크롤링
    Soup = BeautifulSoup(Open_URL, "html.parser")
    try:
        # 크롤링 데이터 중 급식 데이터 만 추출
        Find_Contents = Soup.find(id="contents") # ID 값이 'contents' 인 데이터만 추출
        Find_Table = Find_Contents.find_all("table") # table 이라는 태그를 가진 데이터를 가져온다
        Connect_Table = Find_Table[0] # 'Table' 의 첫 번째 데이터를 가져온다
        Find_tr = Connect_Table.find_all("tr") # 'Table[0]' 의 데이터 안에 있는 tr 태그를 가진 데이터를 추출
        Connect_tr = Find_tr[2] # 'tr' 의 두 번째
        Find_td = Connect_tr.find_all("td") # 'tr' 안에 있는 'td' 태그를 추출

        def Re_Data(Find_td):
            Data_List = str(Find_td)
            Data_List = Data_List.replace('[', '').replace(']', '')
            Data_List = Data_List.replace('<br/>', '\n')
            Data_List = Data_List.replace('<td class="textC last">', '')
            Data_List = Data_List.replace('<td class="textC">', '')
            Data_List = Data_List.replace('</td>', '')
            Data_List = Data_List.replace('.', '').replace(',', '')
            Data_List = Data_List.replace('(h)', '')
            Data_List = re.sub(r"\d", "", Data_List)
            return str(Data_List)

        Pure_MealData[0] = Re_Data(Find_td[1])
        Pure_MealData[1] = Re_Data(Find_td[2])
        Pure_MealData[2] = Re_Data(Find_td[3])
        Pure_MealData[3] = Re_Data(Find_td[4])
        Pure_MealData[4] = Re_Data(Find_td[5])
        Pure_MealData[5] = "토요일은 집에서 맛있는 음식을!"
        Pure_MealData[6] = "일요일이에요! 내일 저를 불러주세요!"

        try:
            Pure_MealData_en[0] = Trans(Re_Data(Find_td[1]))
            Pure_MealData_en[1] = Trans(Re_Data(Find_td[2]))
            Pure_MealData_en[2] = Trans(Re_Data(Find_td[3]))
            Pure_MealData_en[3] = Trans(Re_Data(Find_td[4]))
            Pure_MealData_en[4] = Trans(Re_Data(Find_td[5]))
            Pure_MealData_en[5] = "Saturday is delicious food at home!"
            Pure_MealData_en[6] = "It's Sunday! Call me tomorrow!"
        except:
            Pure_MealData_en[0] = "We don't have any food information."
            Pure_MealData_en[1] = "We don't have any food information."
            Pure_MealData_en[2] = "We don't have any food information."
            Pure_MealData_en[3] = "We don't have any food information."
            Pure_MealData_en[4] = "We don't have any food information."
            Pure_MealData_en[5] = "Saturday is delicious food at home!"
            Pure_MealData_en[6] = "It's Sunday! Call me tomorrow!"

    except:
        Pure_MealData[0] = "급식 정보가 없습니다 ㅠㅠ"
        Pure_MealData[1] = "급식 정보가 없습니다 ㅠㅠ"
        Pure_MealData[2] = "급식 정보가 없습니다 ㅠㅠ"
        Pure_MealData[3] = "급식 정보가 없습니다 ㅠㅠ"
        Pure_MealData[4] = "급식 정보가 없습니다 ㅠㅠ"
        Pure_MealData[5] = "토요일은 집에서 맛있는 음식을!"
        Pure_MealData[6] = "일요일이에요! 내일 저를 불러주세요!"
        
    for index_ko in range(0, 6):
        if ''.join(Pure_MealData[index_ko].split()) == '':
            Pure_MealData[index_ko] = "급식 정보가 없습니다 ㅠㅠ"
        else:
            pass

    for index_en in range(0, 6):
        if ''.join(Pure_MealData_en[index_en].split()) == '':
            Pure_MealData_en[index_en] = "We don't have any food information."
        else:
            pass

    return {"ko":Pure_MealData, "en":Pure_MealData_en}

def MealData_DBin():
    Api_Call = MealData()["ko"]

    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    Mon = Api_Call[0]
    Tue = Api_Call[1]
    Wed = Api_Call[2]
    Thu = Api_Call[3]
    Fri = Api_Call[4]
    Sat = Api_Call[5]
    Sun = Api_Call[6]

    MealData_Neis.objects.create(DateTime=DateTime, Mon=Mon, Tue=Tue, Wed=Wed, Thu=Thu,
                                 Fri=Fri, Sat=Sat, Sun=Sun)

    return "저장 완료"

def MealData_DBin_en():
    Api_Call = MealData()["en"]

    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    Mon = Api_Call[0]
    Tue = Api_Call[1]
    Wed = Api_Call[2]
    Thu = Api_Call[3]
    Fri = Api_Call[4]
    Sat = Api_Call[5]
    Sun = Api_Call[6]

    MealData_Neis_en.objects.create(DateTime=DateTime, Mon=Mon, Tue=Tue, Wed=Wed, Thu=Thu,
                                 Fri=Fri, Sat=Sat, Sun=Sun)

    return "저장 완료"

def API_Call_MealData():
    MealData_DBin()
    MealData_DBin_en()
    return "완료"