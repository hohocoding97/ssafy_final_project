from rest_framework import serializers
from .models import Article, Comment, Reply
from accounts.models import User

class ReplySerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  class Meta:
    model = Reply
    fields = '__all__'
    read_only_fields = ('user', 'comment')

# 댓글리스트
class CommentListSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  reply_set = ReplySerializer(many=True, read_only=True)
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('user','article')

# 게시글 생성 또는 게시글리스트 조회시 사용
class ArticleListSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  comment_set = CommentListSerializer(many=True, read_only=True)
  comment_cnt = serializers.SerializerMethodField()
  class Meta:
    model = Article
    fields ='__all__'

  def get_comment_cnt(self, obj):
        return obj.comment_set.count()


class ArticleDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username', read_only=True)
  comment_set = CommentListSerializer(many=True, read_only=True)
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ('user',)







  