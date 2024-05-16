from rest_framework import serializers
from .models import Movie, UserRating, MovieComment

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

# 영화평점주기 위해
class ratingSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserRating
    fields = '__all__'
    read_only_fields = ('user') #유저는 나중에 저장할거니

# 영화 댓글과 관려된 녀석
class movieCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = MovieComment
    fields ='__all__'
    read_only_fields = ('user', 'movie')
