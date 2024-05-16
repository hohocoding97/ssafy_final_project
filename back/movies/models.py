from django.db import models

# Create your models here.

class Actor(models.Model):
  actor_code = models.IntegerField(primary_key=True) #영화배우의 코드를 pk로 사용
  actor_name = models.TextField()
  profile_path = models.TextField(null=True)

class Director(models.Model):
  director_code = models.IntegerField(primary_key=True)
  director_name = models.TextField()
  
class Genre(models.Model):
  genre_code = models.IntegerField(primary_key=True) #장르 코드를 pk로 사용
  genre_name = models.TextField()
  
class Movie(models.Model):
  code = models.IntegerField(primary_key=True) #영화의 코드를 pk로 사용
  title = models.CharField(max_length = 30)
  score = models.FloatField()
  overview = models.TextField()
  popularity = models.FloatField()
  poster_url = models.TextField()
  release_date = models.DateField()
  actors = models.ManyToManyField(Actor)
  genres = models.ManyToManyField(Genre)
  directors = models.ManyToManyField(Director)