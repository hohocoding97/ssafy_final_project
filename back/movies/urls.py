from django.urls import path
from . import views

urlpatterns = [
    path('create-db/', views.fetch_and_save_popular_movies),
]
