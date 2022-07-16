from django.db import models

# Create your models here.

# 참고로 모델만들었으면 manage.py makemigrations 랑 migrate 해주기!
# 사용자 프로필
class Profile(models.Model):
    # id 값은 자동생성
    name = models.CharField(max_length=10, blank=None, null=True)
    age = models.IntegerField(default=20, blank=None, null=True)
    phone = models.CharField(max_length=20, blank=None, null=True)
    pup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 사용자가 생성한 모임
class Room(models.Model):
    # 사용자가 없어지면 사용자가 생성한 모임도 삭제되도록.
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, blank=None, null=True)
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=10, blank=None, null=True)
    certification_photo = models.ImageField(upload_to = 'certification/', null=True, blank=True)

    def __str__(self):
        return self.title, self.host.name + " 님이 생성한 모임"