from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'accounts'
urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
  path('<int:user_pk>/', views.user_detail),
  path('<int:user_pk>/follow/', views.follow)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
