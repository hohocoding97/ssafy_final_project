from dataclasses import fields
from rest_framework import serializers
from .models import Movie, UserRating, MovieComment, Actor, Genre, Director
from django.contrib.auth import get_user_model
from django.db.models import Avg

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

# 유저가 준 영화 평점
class UserRatingSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserRating
      fields = ('rating')

  
#영화 한번에 쫙 보여 줄때
class movieListSerializer(serializers.ModelSerializer):
  genres = GenreSerializer(many=True, read_only=True)
  class Meta:
    model = Movie
    fields = ('code', 'title', 'poster_url', 'genres')


#영화 디테일 페이지에 필요
class movieDetailSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True, read_only=True)
  genres = GenreSerializer(many=True, read_only=True)
  directors = DirectorSerializer(many=True, read_only=True)

  userrating_set = UserRatingSerializer(many=True, read_only=True) #이게과연 필요한가....??
  average_rating = serializers.SerializerMethodField()
  class Meta:
    model = Movie
    fields = '__all__'

  def get_average_rating(self, obj):
      average = obj.userrating_set.aggregate(Avg('rating')).get('rating__avg')
      return average if average is not None else 0