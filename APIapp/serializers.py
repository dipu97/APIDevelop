from rest_framework import serializers
from .models import APIModel
class APIappSerializers(serializers.ModelSerializer):
    class Meta:
        model=APIModel
        fields= '__all__'