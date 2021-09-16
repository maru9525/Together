from django.db import models


class Party(models.Model):
  party_idx = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100) # 제목
  personnel = models.IntegerField() # 모집 인원
  email = models.EmailField() # 이메일
  password = models.CharField(max_length=100) # 비밀번호
  party_start_date = models.DateTimeField() # 시작일
  party_end_date = models.DateTimeField() # 종료일
  price = models.IntegerField() # 하루 당 이용 요금
  rule_age = models.BooleanField(default=False) # 19세 이상
  rule_assign = models.BooleanField(default=False) # 계정 양도
  rule_share = models.BooleanField(default=False) # 계정 공유
  rull_refund = models.BooleanField(default=False) # 환불
  detail_content = models.TextField() # 상세 내용

  def __str__(self):
    return self.title
