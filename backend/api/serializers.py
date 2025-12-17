from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Period

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PeriodSerializer(serializers. ModelSerializer):
    class Meta:
        model = Period
        fields = ["id", "title", "duration", "created_at", "owner"]
        extra_kwargs = {"owner": {"read_only": True}}
