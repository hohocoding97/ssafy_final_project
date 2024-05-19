from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Movie, UserRating, MovieComment, Actor, Genre, Director
from .serializer import movieListSerializer, movieDetailSerializer, ratingSerializer, movieCommentSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = movieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = movieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST','PUT'])               # 일단은 머리 아프니까 평점 주기만 하자
@permission_classes([IsAuthenticated])  # 로그인한 유저만 사용
def give_a_rating(request, movie_pk):   # 웹 사용자가 평점주기
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        serializer = ratingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 영화 한줄평 조회하기, 영화 한줄평 생성하기
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def movie_comment(request, movie_pk):  
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        serializer = movieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)
    elif request.method == 'GET':
        movies = movie.moviecomment_set.all() # 역참조해서 현 영화의 한줄평들을 다 가져오기
        serializer = movieCommentSerializer(movies, many=True) 
        return Response(serializer.data)

#영화 한줄평 삭제 또는 수정
@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def movie_comment_del_edit(request, movie_comment_pk):
    comment = MovieComment.objects.get(pk=movie_comment_pk)
    if comment.user != request.user:
        return Response('올바르지 않은 접근입니다.', status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        comment.delete()
        return Response('삭제완료',status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = movieCommentSerializer(instance=comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST', 'PUT'])


###################db에 영화 정보 가져오고 저장할 함수#######################
import requests
import datetime
from .models import Movie, Actor, Genre, Director
from django.conf import settings
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
    )
    movie.actors.set(actor_instances)
    movie.directors.set(director_instances)
    movie.genres.set(genre_instances)

def fetch_and_save_popular_movies(request):
    # api_key = settings.TMDB_API_KEY1
    api_key='90aeb74b35c6573b54ef820f2e4944f5'
    for page in range(1,21):
        # url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={page}&region=ko-KR'
        # response = requests.get(url)

        url = f'https://api.themoviedb.org/3/discover/movie?page={page}'
        params = {
            'api_key':'90aeb74b35c6573b54ef820f2e4944f5',
            'language':'ko-KR',
            'region': 'KR',
            'include_adult': False,
            'with_original_language':'ko'
        }
        response=requests.get(url, params=params)

        data = response.json()
        popular_movies = data.get('results', [])
        for movie_data in popular_movies:
            if movie_data['overview']: #영화 설명이 있는 경우만 저장하기
                try:
                    Movie.objects.get(pk=movie_data['id']) # 이미 저장한 영화면은 저장안할수 있게 try-except구문 활용
                except:
                    save_movie_data(request, movie_data)
    

def save_actors(request):
    api_key='90aeb74b35c6573b54ef820f2e4944f5'
    movies = Movie.objects.all()
    for movie in movies:
        url = f'https://api.themoviedb.org/3/movie/{movie.pk}/credits'
        params = { 'api_key': api_key, 'language': 'ko-KR'}

        response = requests.get(url, params=params)
        data = response.json()
        actors = []
        directors = []
        for person_data in data['cast']:
            if person_data['known_for_department'] == 'Acting':
                try:
                    Actor.objects.get(pk=person_data['id'])
                except:                    
                    Actor.objects.create(actor_code=person_data['id'], 
                                        actor_name=person_data['name'],
                                        profile_path=person_data['profile_path'],
                                        popularity=person_data['popularity'])
                    if person_data['id'] not in movie.actors.all():
                        actors.append(person_data['id'])

            elif person_data['known_for_department'] == 'Directing':
                try:
                    Director.objects.get(pk=person_data['id'])
                except:
                    Director.objects.create(director_code=person_data['id'], 
                                            director_name=person_data['name'],)
                    if person_data['id'] not in movie.directors.all():
                        directors.append(person_data['id'])
        movie.actors.set(actors)
        movie.directors.set(directors)

def save_genres(request):
    api_key='90aeb74b35c6573b54ef820f2e4944f5'
    movies = Movie.objects.all()
    for movie in movies:
        url = f'https://api.themoviedb.org/3/movie/{movie.pk}'
        params = { 'api_key': api_key, 'language': 'ko-KR'}
        response = requests.get(url, params=params)
        data = response.json()
        genres = []
        for genre_data in data['genres']:
            try:
                Genre.objects.get(pk=genre_data['id'])
            except:
                Genre.objects.create(genre_code=genre_data['id'], genre_name=genre_data['name'])
                if genre_data['id'] not in movie.genres.all():
                    genres.append(genre_data['id'])
        movie.genres.set(genres)
