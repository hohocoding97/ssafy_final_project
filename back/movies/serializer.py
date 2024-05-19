from dataclasses import fields
from rest_framework import serializers
from .models import Movie, UserRating, MovieComment, Actor, Genre, Director
from django.contrib.auth import get_user_model

#영화 한번에 쫙 보여 줄때
class movieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('code', 'title', 'poster_url')

# 영화평점주기 위해
class ratingSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserRating
    fields = '__all__'
    read_only_fields = ('user') #유저는 나중에 저장할거니

# 영화 댓글과 관려된 녀석
class movieCommentSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = MovieComment
    fields ='__all__'
    read_only_fields = ('user', 'movie')

# 배우 정보
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
# 장르 정보
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
# 감독 정보
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

#영화 디테일 페이지에 필요
class movieDetailSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True, read_only=True)
  genres = GenreSerializer(many=True, read_only=True)
  directors = DirectorSerializer(many=True, read_only=True)

  class Meta:
    model = Movie
    fields = '__all__'

