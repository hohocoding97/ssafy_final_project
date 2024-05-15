from urllib import response
from django.shortcuts import render

# Create your views here.

###################db에 영화 정보 가져오고 저장할 함수#######################
import requests
from .models import Movie, Actor, Genre, Director
from django.conf import settings
from pprint import pprint
from django.http import JsonResponse


def save_movie_data(request,movie_data):
    # 배우 저장
    actors = movie_data.get('actors', [])
    actor_instances = []
    for actor_data in actors:
        actor, created = Actor.objects.get_or_create(actor_name=actor_data['name'])
        actor_instances.append(actor)
    
    # 감독 저장
    directors = movie_data.get('directors', [])
    director_instances = []
    for director_data in directors:
        director, created = Director.objects.get_or_create(director_name=director_data['name'])
        director_instances.append(director)

    # 장르 저장
    genres = movie_data.get('genres', [])
    genre_instances = []
    for genre_data in genres:
        genre, created = Genre.objects.get_or_create(genre=genre_data['name'])
        genre_instances.append(genre)

    # 영화 저장
    movie = Movie.objects.create(
        code=movie_data['id'],
        title=movie_data['title'],
        score=movie_data['vote_average'],
        overview=movie_data['overview'],
        popularity=movie_data['popularity'],
        poster_url=movie_data['poster_path'],
        release_date=movie_data['release_date'],
        # movieCd=movie_data['movieCd']
    )
    movie.actors.set(actor_instances)
    movie.directors.set(director_instances)
    movie.genres.set(genre_instances)

def fetch_and_save_popular_movies(request):
    # api_key = settings.TMDB_API_KEY1
    api_key='90aeb74b35c6573b54ef820f2e4944f5'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    # pprint(data)
    # return JsonResponse(data)
    popular_movies = data.get('results', [])
    for movie_data in popular_movies:
        save_movie_data(request, movie_data)

    return JsonResponse(data)