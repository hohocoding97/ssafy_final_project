from rest_framework import serializers
from django.contrib.auth import get_user_model


# 일단 임시로 확인하는 거임
class userDetailSerializer(serializers.ModelSerializer):
  followers = serializers.SerializerMethodField()
  class Meta:
    model = get_user_model()
    fields = ('id','username','email','followings','followers')
  
  def get_followers(self, obj):
    return obj.followers.values_list('id', 'username')
