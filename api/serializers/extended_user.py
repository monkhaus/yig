from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models.extended_user import ExtendedUserModel
from api.serializers.user import UserSerializer

class ExtendedUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = ExtendedUserModel
        fields = ['user', 'isPremium']