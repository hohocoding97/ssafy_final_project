from functools import partial
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentListSerializer



@api_view(['GET','POST'])
def ariticle_list(request):
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
      serializer = ArticleDetailSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시글 디테일 확인
@api_view(['GET',])
def article_detail(request, article_pk):
  if request.method == 'GET':
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 게시글 수정 또는 삭제 
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_ud(request, article_pk):
  article = Article.objects.get(pk=article_pk) 
  if request.method == 'PUT':
    serializer = ArticleDetailSerializer(instance=article,data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    
  elif request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 댓글 조회
@api_view(['GET'])
def comment_list(request, article_pk):
  if request.method == 'GET':
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
  pass

