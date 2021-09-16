from .models import Party
from rest_framework.serializers import ModelSerializer

class PartySerializer(ModelSerializer):
  class Meta:
    model = Party
    fields = '__all__'