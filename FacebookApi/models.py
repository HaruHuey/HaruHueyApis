from django.db import models

# Create your models here.

# 페이스북 API 로그 데이터
class LogData(models.Model):
    # 시간
    DateTime = models.CharField(max_length=23)
    # 로그 타입
    Log_Type = models.CharField(max_length=10)
    # 내용 데이터
    Data = models.CharField(max_length=200)
    # 기타 내용
    TextData = models.TextField(null=True)