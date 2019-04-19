import urllib.request
import json
from DatabasePy.Trans_Papago import Trans
import datetime
from DatabasePy.models import Weather_skplanet, Weather_skplanet_en

def Weather_Skplanet():
    # 학교 좌표 값으로 주변 날씨 호출 / API KEY +
    Weather_URL = "https://api2.sktelecom.com/weather/current/minutely?version=2&lat=37.6421104&lon=127.0596316&appKey=125e2dfe-2633-4bd4-b268-7e9a4f24f6c3"

    # 날씨 API URL 열기 * 시간 초과 5초
    # 한글 인코딩 오류 이슈
    # .decode("utf-8")을 코드에 추가해서 크롤링된 데이터 깨짐 방지
    Open_URL_Weather = urllib.request.urlopen(Weather_URL, timeout=10).read().decode("utf-8")

    # JSON 로딩
    Json_Load_Weather = json.loads(Open_URL_Weather)
    Weather_Json = Json_Load_Weather["weather"]["minutely"][0]

    # JSON 데이터 변수
    station_name = Weather_Json["station"]["name"]
    station_type = Weather_Json["station"]["type"]
    wind_wdir = Weather_Json["wind"]["wdir"]
    wind_wspd = Weather_Json["wind"]["wspd"]
    snowrain_sinceOntime = Weather_Json["precipitation"]["sinceOntime"]
    snowrain_type = Weather_Json["precipitation"]["type"]
    sky_name = Weather_Json["sky"]["name"]
    rain_sinceMidnight = Weather_Json["rain"]["sinceMidnight"]
    temperature_tc = Weather_Json["temperature"]["tc"]
    temperature_tmax = Weather_Json["temperature"]["tmax"]
    temperature_tmin = Weather_Json["temperature"]["tmin"]
    humidity = Weather_Json["humidity"]
    pressure_surface = Weather_Json["pressure"]["surface"]

    try:
        station_name_en = Trans(station_name)
        sky_name_en = Trans(sky_name)
    except:
        station_name_en = "-"
        sky_name_en = "-"

    DateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    Date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    Time = str(datetime.datetime.now().strftime("%H:%M"))

    Weather_skplanet.objects.create(DateTime=DateTime, Date=Date, Time=Time, station_name=station_name,
                                    station_type=station_type, wind_wdir=wind_wdir, wind_wspd=wind_wspd,
                                    snowrain_sinceOntime=snowrain_sinceOntime, snowrain_type=snowrain_type,
                                    sky_name=sky_name, rain_sinceMidnight=rain_sinceMidnight,
                                    temperature_tc=temperature_tc, temperature_tmax=temperature_tmax,
                                    temperature_tmin=temperature_tmin, humidity=humidity, pressure_surface=pressure_surface)

    Weather_skplanet_en.objects.create(DateTime=DateTime, Date=Date, Time=Time, station_name=station_name_en,
                                       station_type=station_type, wind_wdir=wind_wdir, wind_wspd=wind_wspd,
                                       snowrain_sinceOntime=snowrain_sinceOntime, snowrain_type=snowrain_type,
                                       sky_name=sky_name_en, rain_sinceMidnight=rain_sinceMidnight,
                                       temperature_tc=temperature_tc, temperature_tmax=temperature_tmax,
                                       temperature_tmin=temperature_tmin, humidity=humidity, pressure_surface=pressure_surface)

    return "저장 완료"