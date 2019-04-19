# 날씨 이미지 처리
import datetime

from DatabasePy.models import Weather_skplanet, Weather_skplanet_en

def WeatherIMG_DB(sky_name):
    time_con = datetime.datetime.now().strftime('%H')
    time_dt = int(time_con)
    if time_dt in [1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 23, 24]:
        time_code = "Night"
    elif time_dt in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
        time_code = "Day"
    else:
        time_code = "Day"

    if "맑음" in sky_name:
        Night = 'https://i.imgur.com/eF2beP4.png" title="Night_Sun.png'
        Day = 'https://i.imgur.com/2O0UmID.png" title="Day_Sun.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "구름조금" in sky_name:
        Night = 'https://i.imgur.com/iipLDIl.png" title="Night_SunandCloud.png'
        Day = 'https://i.imgur.com/IBk6mvx.png" title="Day_SunandCloud.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "구름많음" in sky_name:
        Night = 'https://i.imgur.com/9mbnOaw.png" title="Night_Cloud.png'
        Day = 'https://i.imgur.com/MnfpabY.png" title="Day_Cloud.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "구름많고 비" in sky_name:
        Night = 'https://i.imgur.com/5dLmtmk.png" title="Day_rain.png'
        Day = 'https://i.imgur.com/wdqMpCu.png" title="Night_rain.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "구름많고 눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "구름많고 비 또는 눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "흐림" in sky_name:
        Night = 'https://i.imgur.com/egcK9Uh.png" title="Night_Soso.png'
        Day = 'https://i.imgur.com/hhSwgtS.png" title="Day_Soso.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "흐리고 비" in sky_name:
        Night = 'https://i.imgur.com/5dLmtmk.png" title="Day_rain.png'
        Day = 'https://i.imgur.com/wdqMpCu.png" title="Night_rain.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "흐리고 눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "흐리고 비 또는 눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "흐리고 낙뢰" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "뇌우/비" in sky_name:
        Night = 'https://i.imgur.com/5dLmtmk.png" title="Day_rain.png'
        Day = 'https://i.imgur.com/wdqMpCu.png" title="Night_rain.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "뇌우/눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    elif "뇌우/비 또는 눈" in sky_name:
        Night = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        Day = 'https://i.imgur.com/nw0jbdM.png" title="seoulit_logo.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn
    
    # 데이터를 불러오지 못했습니다. 이미지 리턴
    else:
        Night = 'https://i.imgur.com/eF2beP4.png" title="Night_Sun.png'
        Day = 'https://i.imgur.com/2O0UmID.png" title="Day_Sun.png'
        urlReturn = Night if time_code == "Night" else Day
        return urlReturn