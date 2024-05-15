from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:pk>/', views.movie_detail),
    path('create-db/', views.fetch_and_save_popular_movies),
]
