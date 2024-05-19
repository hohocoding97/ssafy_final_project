from django.urls import path
from . import views

urlpatterns = [
  path('article/', views.ariticle_list), 
  path('article/<int:article_pk>/', views.article_detail),
  path('article/<int:article_pk>/ud/',views.article_ud),
  path('comment/<int:article_pk>/',views.comment_list),
  path('comment/<int:article_pk>/create/',views.create_comment),
  path('comment/<int:comment_pk>/ud/',views.comment_ud),
  path('reply/<int:comment_pk>/', views.reply), #대댓글 작성
  path('reply_ud/<int:reply_pk>/',views.reply_ud), #대댓글 수정 삭제
]
