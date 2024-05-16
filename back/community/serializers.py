from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ('user', 'title', 'created_at')

class ArticleDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ('user',)

