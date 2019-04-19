from django.db import models

# Create your models here.

# DialogFlowApi 로그 데이터
class LogData(models.Model):
    # 시간
    DateTime = models.CharField(max_length=23)
    # 로그 타입
    Log_Type = models.CharField(max_length=10)
    # 내용 데이터
    Data = models.CharField(max_length=200)
    # 기타 내용
    TextData = models.TextField(null=True)

# 개별 로그 데이터 수집
class reqLog(models.Model):
    # 시간
    DateTime = models.CharField(max_length=23)

    # 개인 식별 ID
    responseId_req = models.CharField(max_length=50)

    # 받은 데이터
    queryText_req = models.CharField(max_length=300)

    # 파라메터 정보
    param_req = models.CharField(max_length=500)

    # 언어 코드
    languageCode_req = models.CharField(max_length=10)

    # 문장 의도 분석 값
    intent_displayName_req = models.CharField(max_length=100)