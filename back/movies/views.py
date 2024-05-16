from django.shortcuts import render
from .serializer import movieListSerializer, movieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

###################db에 영화 정보 가져오고 저장할 함수#######################
import requests
import datetime
from .models import Movie, Actor, Genre, Director
from django.conf import settings
from pprint import pprint
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
    for page in range(1,21):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={page}&region=ko-KR'
        response = requests.get(url)
        data = response.json()
        popular_movies = data.get('results', [])
        for movie_data in popular_movies:
            save_movie_data(request, movie_data)
    


###################한국영화진흥위원회 박스오피스 데이터 가져오기(미완..)##########################

def save_kobis_movie(request, data):
    dates = make_date()

    return

def fectch_and_save_kobis_movie(request):
    movie_dict = {}
    api_key = "c749cadac1d9f0a8006aa2267c7210e2"
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
    dates = make_date()
    for date in dates:
        payload = {
        "key": api_key,
        "targetDt": date,  # 조회하고자 하는 날짜 (예시 날짜)
        "weekGb": "0",  # 주간 (월~일)
        "itemPerPage": "10",  # 결과 ROW의 개수(최대 : 10개)
        "multiMovieYn": "N",  # 상업영화
        # "repNationCd": "K",  # 한국영화(default:전체)
        # "wideAreaCd": ""  # 전체 지역
        }
        response = requests.get(base_url, params=payload)
        data = response.json()
        
        for movie in data.get('weeklyBoxOfficeList'):
            if movie_dict.get(movie.get('movieCd')): #만약 movieCd를 key로 하는 쌍이 있으면
                movie['movieCd']

def make_date(request):
    # 시작일과 종료일 설정
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2024, 1, 1)  # 2024년 1월 1일 전까지만

    # 7일 간격으로 날짜 생성하여 리스트에 저장
    dates_list = []
    current_date = start_date
    while current_date < end_date:
        dates_list.append(current_date.strftime("%Y%m%d"))
        current_date += datetime.timedelta(days=7)
