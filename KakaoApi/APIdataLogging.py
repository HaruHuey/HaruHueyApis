# API Data 통신 로깅
# 추후 문제 및 보안으로 인해 데이터 수집
import json

from KakaoApi.models import reqLog

def APIdataLogging(LoadJson_req):
    # created_at = models.DateTimeField(auto_now_add=True)
    # userRequest 사용자 발화 블록 정보
    try:
        block_name = str(LoadJson_req["userRequest"]["block"]["name"])
    except:
        block_name = "Non-Data"

    # userRequest 사용자가 작성한 발화
    try:
        utterance = str(LoadJson_req["userRequest"]["utterance"])
    except:
        utterance = "Non-Data"

    # userRequest user 유저 - 봇 UserId(Key)
    try:
        bot_userID = str(LoadJson_req["userRequest"]["user"]["id"])
    except:
        bot_userID = "Non-Data"

    # userRequest user properties - 플러스 친구 사용자 id
    try:
        plusfriendUserKey = str(LoadJson_req["userRequest"]["user"]["properties"]["plusfriendUserKey"])
    except:
        plusfriendUserKey = "Non-Data"

    # userRequest user properties - 카카오 ID
    try:
        appUserId = str(LoadJson_req["userRequest"]["user"]["properties"]["appUserId"])
    except:
        appUserId = "Non-Data"

    # action detailParams - JSON 형태 로그
    try:
        detailParams = LoadJson_req["action"]["detailParams"]
    except:
        detailParams = {
            'NonData': 'Non-Data'
        }

    try:
        reqLog.objects.create(
            block_name=block_name,
            utterance=utterance,
            bot_userID=bot_userID,
            plusfriendUserKey=plusfriendUserKey,
            appUserId=appUserId,
            detailParams=detailParams
        )
    except:
        pass

    return "저장 완료"