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

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model=User
        fields=['username','password']
    
    def create(self,validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )