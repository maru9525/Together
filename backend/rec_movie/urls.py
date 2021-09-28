from django.urls import path, include
from . import views
from rest_framework import routers  # router import

app_name = 'movieApp'    # URL 네임스페이스

urlpatterns = [
    path('get-json/', views.getMovieData),
    path('get-review/', views.getReviewData),

]
