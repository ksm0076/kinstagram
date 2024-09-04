from django.db import models

# Create your models here.
class Feed(models.Model):
    user_email = models.TextField() # 작성자
    image = models.TextField() # 올린 사진
    content = models.TextField() # 글 내용

class comment(models.Model):
    feed_id = models.IntegerField(default=0) # 피드의 id
    email = models.EmailField(default='') # 댓글 작성한 사람
    nickname = models.TextField(default='') # 댓글 작성한 사람 닉네임
    comment_content = models.TextField() # 댓글 내용
    
class like(models.Model):
    feed_id = models.IntegerField(default=0) # 피드 id
    email = models.EmailField(default='') # 좋아요 누른 사람 이메일
    nickname = models.TextField(default='') # 좋아요 누른 사람 닉네임
    is_like = models.BooleanField(default=True) # 좋아요 여부
    
class bookmark(models.Model):
    feed_id = models.IntegerField(default=0) # 피드 id
    email = models.EmailField(default='') # 북마크 누른 사람
    nickname = models.TextField(default='') # 북마크 누른 사람 닉네임
    is_bookmark = models.BooleanField(default=True) # 북마크 여부