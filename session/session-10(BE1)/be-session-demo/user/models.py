from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# 유저 매니징 할 수 있음. ; 적절하게 오버라이드 해서 사용할 수 있다.
# class ServiceUserManager(UserManager):
#     # _ : 자바의 제어자.(protected) 
#     def _create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#     def create_user(self, usernema, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
        


# class Serviceuser(AbstractUser):
#     phone =models.CharField(verbose_name="전화번호", max_length=11, default="010000000000", null=True)

    # objects = Serviceuser()