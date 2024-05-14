from django.db import models

# Create your models here.

class Actor(models.Model):
  actor_name = models.TextField()
  filmo = models.TextField()
  
class Director(models.Model):
  director_name = models.TextField()
  
class Genre(models.Model):
  genre = models.TextField()
  
class Movie(models.Model):
  movie_id = models.IntegerField()
  title = models.CharField(max_length = 30)
  score = models.FloatField()
  overview = models.TextField()
  popularity = models.FloatField()
  poster_url = models.TextField()
  release_date = models.DateField()
  movieCd = models.IntegerField()
  actors = models.ManyToManyField(Actor)
  genre = models.TextField(Genre)
  directors = models.ManyToManyField(Director)

  
