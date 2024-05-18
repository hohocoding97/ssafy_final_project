from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:pk>/', views.movie_detail),
    path('<int:movie_pk>/rating/', views.give_a_rating), #영화 평점주기
    path('<int:movie_pk>/create_check_comment/', views.movie_comment), #영화 한줄평쓰기
    path('<int:movie_comment_pk>/comment/', views.movie_comment_del_edit), #영화한줄평 삭제또는 수정
    path('create-db/', views.fetch_and_save_popular_movies), #일단 영화 db 받는 url 
    path('create-actors-db/', views.save_actors), #영화 db받은 후 배우 정보 저장하는 url
    path('create-genres-db/', views.save_genres) 
]