from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from drf_react_gems_backend.user_credentials.models import (
    UserCredentials,
)
from drf_react_gems_backend.user_profile.models import (
    UserProfile,
)


class RegisterUserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password")

        return data

    def validate(self, attrs):
        password = attrs.get("password", None)
        try:
            validate_password(password)
        finally:
            return attrs

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]

        user_credentials = UserCredentials.objects.create(
            email=email,
            password=make_password(password),
        )

        UserProfile.objects.create(
            user=user_credentials,
            first_name=first_name,
            last_name=last_name,
        )

        return user_credentials
