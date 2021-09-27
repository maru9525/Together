from django.urls import path
from . import views

urlpatterns = [
  path('party/', views.PartyView.as_view()),
  path('party/<int:party_idx>/', views.PartyDetailView.as_view()),
  path('party/<int:party_idx>/join', views.PartyDetailView.as_view()),
]