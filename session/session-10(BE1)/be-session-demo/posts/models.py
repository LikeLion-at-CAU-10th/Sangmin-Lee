from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    # 반복해서 쓰는 걸 abstract 해서 상속해서 사용하기.
    class Meta:
        abstract = True

class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    post_id = models.AutoField(primary_key=True)
    # admin에서 verbose_name 에 저장된 이름으로 보임.
    profile_image = models.ImageField(
        verbose_name='프로필 사진', null=True, blank=True)
    writer = models.CharField(verbose_name="작성자", max_length=30)
    content = models.TextField(verbose_name="내용")
    category = models.CharField(choices=CHOICES, max_length=20)
 

class Comment(BaseModel):
    writer = models.CharField(verbose_name="작성자", max_length=30)
    content = models.CharField(verbose_name="내용", max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, blank=False)

    
