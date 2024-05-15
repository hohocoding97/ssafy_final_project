from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 내가 팔로우하는 사람들 (followings): 참조
    # 나를 팔로우 하는 사람들(followers): 역참조