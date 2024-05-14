import requests
import json
import pprint
from django.conf import settings


def get_popular_movies(api_key, page=1):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None
  
api_key= '90aeb74b35c6573b54ef820f2e4944f5'

popular_movies = get_popular_movies(api_key)

if popular_movies:
    for movie in popular_movies['results']:
        print(movie)
else:
    print("인기 영화를 가져오는 데 실패했습니다.")