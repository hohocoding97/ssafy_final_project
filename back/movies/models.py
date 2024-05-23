from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Actor(models.Model):
  actor_code = models.IntegerField(primary_key=True) #영화배우의 코드를 pk로 사용
  actor_name = models.TextField()
  profile_path = models.TextField(null=True)
  popularity = models.FloatField()

class Director(models.Model):
  director_code = models.IntegerField(primary_key=True)
  director_name = models.TextField()
  profile_path = models.TextField(null=True)
  
class Genre(models.Model):
  genre_code = models.IntegerField(primary_key=True) #장르 코드를 pk로 사용
  genre_name = models.TextField()


class Movie(models.Model):
  code = models.IntegerField(primary_key=True) #영화의 코드를 pk로 사용
  title = models.CharField(max_length = 40)
  score = models.FloatField()
  overview = models.TextField()
  popularity = models.FloatField()
  poster_url = models.TextField()
  release_date = models.DateField()
  actors = models.ManyToManyField(Actor)
  genres = models.ManyToManyField(Genre)
  directors = models.ManyToManyField(Director)


class Trailer(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='trailers')
  url = models.TextField()


class UserRating(models.Model): #우리 웹사이트 이용자가 준 평점
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)]) # 1~10사이의 정수만

class MovieComment(models.Model): #영화에 대한 댓글
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  content = models.CharField(max_length = 50)