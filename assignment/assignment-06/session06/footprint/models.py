from django.db import models

# Create your models here.

# 클래스명은 대문자로 시작.
# 매개변수 이런 거 외울 필요 없다.

class Footprint(models.Model):
    # AutoField 자동으로 숫자하나 증가해서 식별하는 데 좋다. DB설계할 때 유용
    footprint_id = models.AutoField(primary_key=True)
    # 리시버 없는 건 거짓이다. 오류 방지위해
    receiver = models.TextField(null=False)
    message = models.TextField(null=False)
    # 메세지가 언제 보내는지 파악하기 위해 
    sent_at = models.DateTimeField(auto_now_add=True, blank=False)

    