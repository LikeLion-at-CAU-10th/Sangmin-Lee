
from django.db import models

# Create your models here.

# class LikeLion(models.Model):
#     CHOICE = (
#         ('기획', "기획"),
#         ('백엔드', "백엔드"),
#         ('프론트엔드', "프론트엔드"),

#     )
#     # unique=True ; 같은 이름으로 안말들어짐.
#     name = models.CharField(max_length=20, default="", unique=True)
#     # choice 선택지 중에 고를 수 있게됨.
#     part = models.CharField(max_length=20, choices=CHOICE, default="백엔드")
#     # 음수일 때 받기 싫을 때 POSITIVE INT

#     age = models.IntegerField(default=20)
#     bio = models.TextField(default="소개를 입력해주세요", null=True)
#     # 사진에 max_length ; 가질 수 있는 사진 수
#     profile_image = models.ImageField(max_length=5, null=True, blanck=True)
class LikeLion(models.Model):
    CHOICES = (
        ('기획', '기획'),
        ('백엔드', '백엔드'),
        ('프론트엔드', '프론트엔드')
    ) 
    name = models.CharField(max_length=20, default="", unique=True)
    part = models.CharField(max_length=20, choices=CHOICES, default="백엔드")
    age = models.IntegerField(default=20)
    bio = models.TextField(default="소개를 입력해주세요.", null=True)
    profile_image = models.ImageField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.name

class Management(models.Model):
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=20)