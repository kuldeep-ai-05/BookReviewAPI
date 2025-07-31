from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book , Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    reviewer=UserSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'

    def create(self,validated_data):
        validated_data['reviewer']= self.context['request'].user
        return super().create(validated_data)
