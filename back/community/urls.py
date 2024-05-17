from django.urls import path
from . import views

urlpatterns = [
  path('article/', views.ariticle_list), 
  path('article/<int:article_pk>/', views.article_detail),
  path('article/<int:article_pk>/ud/',views.article_ud),
  path('comment/<int:article_pk>/',views.comment_list),
]
