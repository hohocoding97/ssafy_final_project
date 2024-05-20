from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import userDetailSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# 유저 디테일 정보 확인하기 또는 수정하기
@api_view(['GET', 'PUT'])
def user_detail(request, user_pk):
  user = get_user_model().objects.get(pk=user_pk)
  if request.method == 'GET':
    serializer = userDetailSerializer(user)
    return Response(serializer.data)
  elif request.method == 'PUT':
     serializer = userDetailSerializer(instance=user, data=request.data, partial=True)
     if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# follow 또는 unfollow
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    me = request.user
    you = get_user_model().objects.get(pk=user_pk)
    if you in me.followings.all():  #만약 이미 팔로우 했다면
        me.followings.remove(you)   #팔로우 취소
        return Response(f'{me.username}이 {you.username}을 팔로우 취소함', status=status.HTTP_200_OK)
    else:
        me.followings.add(you)  #팔로우하기
        return Response(f'{me.username}이 {you.username}을 팔로우함', status=status.HTTP_200_OK)