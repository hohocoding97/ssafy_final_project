from rest_framework import serializers
from .models import Article, Comment, Reply
from accounts.models import User


# 게시글 생성 또는 게시글리스트 조회시 사용
class ArticleListSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = Article
    fields = ('user', 'title', 'created_at','username')
  

class ArticleDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ('user',)

class CommentListSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('user','article')

class ReplySerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = Reply
    fields = '__all__'
    read_only_fields = ('user', 'comment')
  