from pyexpat import model
from rest_framework import serializers
from .models import Movie

#영화 디테일 페이지에 필요
class movieDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    # fields = '__all__'
    exclude = ('actors', 'genres', 'directors') #일단 배우정보, 장르정보, 감독정보 없으니까 제외

#영화 한번에 쫙 보여 줄때
class movieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('code', 'title', 'poster_url')

