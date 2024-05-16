from django.urls import path
from . import views

urlpatterns = [
  path('', views.ariticle_list),
  path('<int:article_pk>/', views.article_detail)
]
