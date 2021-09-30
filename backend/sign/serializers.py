from django.db import transaction
from django.db.models import fields
from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
# from dj_rest_auth.serializers import UserDetailsSerializer
# from dj_rest_auth.serializers import LoginSerializer

class UserRegisterSerializer(RegisterSerializer):
  phone_number = serializers.CharField(max_length=20)
  nick_name = serializers.CharField(max_length=100)
  password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

  class Meta:
    model = User
    fields = ['name', 'email', 'password', 'password2', 'phone_number', 'nick_name',]
    extra_kwarge= {
      'password': {
        'write_only': True
      }
    }
  def save(self):
    user = User(
      name = self.validated_data['name'],
      email = self.validated_data['email'],
      nick_name = self.validated_data['nick_name'],
      phone_number = self.validated_data['phone_number'],
      is_active = self.validated_data['is_active'],
      is_admin = self.validated_data['is_admin'],
    )
    password = self.validated_data['password']
    password2 = self.validated_data['password2']

    if password != password2:
      raise serializers.ValidationError({'password': 'Passwords must match.'})
    user.set_password(password)
    user.save()
    return user


# class CustomRegisterSerializer(RegisterSerializer):
#   phone_number = serializers.CharField(max_length=30)
#   nickname = serializers.CharField(max_length=100)

#   @transaction.atomic
#   def save(self, request):
#     user = super().save(request)
#     user.phone_number = self.data.get('phone_number')
#     user.nickname = self.data.get('nickname')
#     user.save()
#     return user

# class CustomUserDetailSerializer(UserDetailsSerializer):
  
#   class Meta:
#     model = User
#     fields = (
#       'pk',
#       'email',
#       'nickname',
#       'username',
#       'phone_number',
#     )
#     read_only_fields = ('pk', 'email','username',)
