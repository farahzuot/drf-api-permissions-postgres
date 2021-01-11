from rest_framework import serializers

from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'describtion', 'author')
        model = Service