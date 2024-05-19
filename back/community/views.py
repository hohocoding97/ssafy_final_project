import stat
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Article, Comment, Reply
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentListSerializer, ReplySerializer


#게시글 생성 또는 게시글리스트 조회
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
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 작성
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_comment(request, article_pk):
  if request.method == 'POST':
    article = Article.objects.get(pk=article_pk)
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, article=article)
      return Response(serializer.data)

#댓글 수정, 삭제
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment_ud(request, comment_pk):
  comment = Comment.objects.get(pk=comment_pk) 
  if request.method == 'PUT':
    serializer = CommentListSerializer(instance=comment,data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    
  elif request.method == 'DELETE':
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
# 대댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply(request, comment_pk): 
  if request.method == 'POST':
    comment = Comment.objects.get(pk=comment_pk)
    serializer = ReplySerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, comment=comment)
      return Response(serializer.data,status=status.HTTP_201_CREATED)

# 대댓글 수정 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def reply_ud(request, reply_pk):
  reply = Reply.objects.get(pk=reply_pk)
  if reply.user != request.user:
    return Response('잘못된 요청입니다', status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'PUT':
    serializer = ReplySerializer(instance=reply, data=request.data, partial= True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'DELETE':
    reply.delete(reply)
    return Response(status=status.HTTP_204_NO_CONTENT)