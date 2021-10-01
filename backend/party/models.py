from django.db import models
from django.conf import settings
from argon2 import PasswordHasher

class Party(models.Model):
  host = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='host')
  title = models.CharField(max_length=100) # 제목
  member_limit = models.IntegerField() # 모집 인원
  service_id = models.EmailField() # 서비스 계정
  service_password = models.CharField(max_length=100) # 비밀번호
  end_date = models.DateTimeField() # 종료일
  price_per_day = models.PositiveIntegerField() # 하루 당 이용 요금
  desc = models.TextField() # 상세 내용
  

  def __str__(self):
    return self.title
