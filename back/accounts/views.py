from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import userDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def user_detail(request, user_pk):
  user = get_user_model().objects.get(pk=user_pk)
  serializer = userDetailSerializer(user)
  return Response(serializer.data)
