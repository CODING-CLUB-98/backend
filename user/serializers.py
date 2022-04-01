from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'image',
            'semester',
            'rollno',
            'phone',
            'image',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'profile'
        )