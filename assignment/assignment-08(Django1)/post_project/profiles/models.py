from django.db import models

# Create your models here.

# 참고로 모델만들었으면 manage.py makemigrations 랑 migrate 해주기!
class Profile(models.Model):
    # id 값은 자동생성
    name = models.CharField(max_length=10, blank=None, null=True)
    age = models.IntegerField(default=20, blank=None, null=True)
    phone = models.CharField(max_length=20, blank=None, null=True)
    pup_date = models.DateField(auto_now_add=True)

