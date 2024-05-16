from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #게시글 작성자
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updataed_at = models.DateTimeField(auto_now=True)

class Comment(models.Model): #게시글 댓글
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #댓글 작성자
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE) #댓글. 어디 댓글의 대댓글인지 알아야하니까
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #대댓글 작성자
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)