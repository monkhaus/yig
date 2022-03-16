from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models.extended_user import ExtendedUserModel

class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUserModel
        fields = ['user', 'isPremium']