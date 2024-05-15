from tkinter import CASCADE
from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #게시글 작성자
    title = models.CharField(max_length=50)
    content = models.TextField()


