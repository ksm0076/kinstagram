from django.db import models

# Create your models here.
class Feed(models.Model):
    profile_image = models.TextField() # 프로필사진
    user_id = models.TextField() # 작성자 닉네임
    image = models.TextField() # 올린사진
    content = models.TextField() # 글내용
    like_count = models.IntegerField() # 좋아요수