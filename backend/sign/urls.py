from django.urls import path
from . import views
from rest_framework import routers    # router import

app_name = 'sign'

urlpatterns = [
    path('', views.index)
]