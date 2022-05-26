from django.db import models

# 클래스명은 대문자로 시작.
# 매개변수 이런 거 외울 필요 없다.

# 사용자 정보 관련 model 정의 ; 
class Account(models.Model):
    # AutoField 자동으로 숫자하나 증가해서 식별하는 데 좋다. DB설계할 때 유용
    account_id = models.AutoField(primary_key=True)
    # 닉네임
    nickname = models.TextField(null=False)
    # mbti
    mbti = models.TextField(null=False)
    # 전공
    major = models.TextField(null=False)
    # 메세지가 언제 보내는지 파악하기 위해 
    sent_at = models.DateTimeField(auto_now_add=True, blank=False)