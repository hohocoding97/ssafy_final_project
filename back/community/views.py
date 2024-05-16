from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


# 게시글 작성과 조회를 그냥 로그인된 사용자만 가능하도록 함
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def ariticle_list(request):
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
      # print('#############',request.user)
      serializer = ArticleDetailSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
  if request.method == 'GET':
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)
  
