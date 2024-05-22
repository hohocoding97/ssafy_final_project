from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers import movieListSerializer

# 유저 디테일 정보 넘겨주기
class userDetailSerializer(serializers.ModelSerializer):
  followers = serializers.SerializerMethodField()
  image_url = serializers.SerializerMethodField()
  # like_movies = movieListSerializer(many=True, read_only=True)
  
  class Meta:
    model = get_user_model()
    fields = ('username','id','image_url','email','nick_name','like_movies', 'followers', 'image_url')
  def get_followers(self, obj):
    return obj.followers.values('id', 'username')
  
  def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

class userLikeMoviesSerializer(serializers.ModelSerializer):
  like_movies = movieListSerializer(many=True, read_only=True)
  class Meta:
     model= get_user_model()
     fields = '__all__'