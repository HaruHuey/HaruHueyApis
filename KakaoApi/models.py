from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

# 카카오 API 로그 데이터
class LogData(models.Model):
    # 시간
    DateTime = models.CharField(max_length=23)
    # 로그 타입
    Log_Type = models.CharField(max_length=10)
    # 내용 데이터
    Data = models.CharField(max_length=200)
    # 기타 내용
    TextData = models.TextField(null=True)

class reqLog(models.Model):
    # 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # userRequest 사용자 발화 블록 정보
    block_name = models.CharField(max_length=50)
    # userRequest 사용자가 작성한 발화
    utterance = models.TextField(null=True)
    # userRequest user 유저 - 봇 UserId(Key)
    bot_userID = models.CharField(max_length=100)
    # userRequest user properties - 플러스 친구 사용자 id
    plusfriendUserKey = models.CharField(max_length=50)
    # userRequest user properties - 카카오 ID
    appUserId = models.CharField(max_length=50)
    # action detailParams - JSON 형태 로그
    detailParams = JSONField(null=True)

    def __str__(self):
        return self.name