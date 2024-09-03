from django.db import models

# Create your models here.
class Feed(models.Model):
    user_email = models.TextField() # 작성자
    image = models.TextField() # 올린사진
    content = models.TextField() # 글내용