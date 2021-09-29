from django.urls import path, include
from . import views
from rest_framework import routers  # router import

app_name = 'movieApp'    # URL 네임스페이스

urlpatterns = [
    path('get-json/', views.get_movie_data),
    path('get-review/', views.get_review_data),
    path('get-genre/', views.get_genre_data),
    path('get-provider/', views.get_provider_data),

]
