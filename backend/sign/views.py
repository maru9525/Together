from django.shortcuts import redirect, render
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets

def passwordResetConfirm(request, uid, token):
  return redirect(f'http://localhost:8080/auth/change-password/{uid}/token/{token}/')


class UserMe(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  def get_queryset(self):
    user = self.request.user
    return User.objects.get_queryset().filter(username=user)
 
