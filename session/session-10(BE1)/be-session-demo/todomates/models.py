from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, DateField, NullBooleanField

# Create your models here.
class Category(models.Model):
    # id ; 설정안해도 쟝고에서 pk 알아서 저장해줌.
    title = models.CharField(max_length=50, default="호호" ,blank=None, null=True)
    view_auth = models.IntegerField(default=0,null=True, blank=None)
    color = models.CharField(max_length=10, default='#000000',null=True, blank=None)
    pup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=20, null=True, blank=True)
    thumb_nail = models.ImageField(upload_to = 'todo/', null=True, blank=True)
    # 0,1로 구분해도 되는데 이번엔 불리안으로
    is_completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    # 변경될때마다 업데이트
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
# 마이그레이션 로그 지우고 db도 지워서 싱크 맞춰야하는 경우