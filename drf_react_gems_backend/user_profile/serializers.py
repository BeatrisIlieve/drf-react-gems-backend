from rest_framework import serializers

from rest_framework import serializers
from drf_react_gems_backend.user_credentials.models import UserCredentials
from drf_react_gems_backend.user_profile.models import UserProfile


class CreateUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()

    class Meta:
        model = UserProfile
        fields = ["user_id", "first_name", "last_name"]

    def validate_user_id(self, value):
        """
        Ensure the user with the given user_id exists.
        """
        try:
            user = UserCredentials.objects.get(pk=value)
        except UserCredentials.DoesNotExist:
            raise serializers.ValidationError("The provided user ID does not exist.")
        return value

    def create(self, validated_data):

        user_id = validated_data.get("user_id")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")

        user = UserCredentials.objects.get(pk=user_id)

        user_profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
        )

        return user_profile
