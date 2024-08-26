from django.db import models

from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class user(AbstractBaseUser):    
    user_email = models.EmailField(unique=True) # 유저 이메일 주소 (회원가입할때 사용하는 아이디)
    # user_password  # 유저 비밀번호
    user_name = models.CharField(max_length=20) # 유저 실제이름
    user_nickname = models.CharField(max_length=20, unique=True) # 유저 닉네임
    profile_img = models.TextField() # 유저 프로필 사진
    
    USERNAME_FIELD = 'user_nickname'
    
    class Meta: # 테이블 이름
        db_table = "user"