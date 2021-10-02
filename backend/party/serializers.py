from .models import Party
from rest_framework import serializers
from sign.serializers import UserSerializer
from argon2 import PasswordHasher


class PartySerializer(serializers.ModelSerializer):
  host = UserSerializer(read_only=True, many=True)

  class Meta:
    model = Party
    fields = '__all__'
    read_only_field = ('host', 'payments')
   