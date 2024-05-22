from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'accounts'
urlpatterns = [
  path('', views.user_detail),
  path('<int:user_pk>/', views.other_user_detail),
  path('<int:user_pk>/follow/', views.follow),
  path('<int:user_pk>/like_movies/', views.like_movies),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
