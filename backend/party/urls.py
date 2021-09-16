from django.urls import path
from . import views

urlpatterns = [
  path('party/', views.PartyView.as_view()),
  path('party/<int:party_idx>/', views.PartyDetail.as_view()),
]