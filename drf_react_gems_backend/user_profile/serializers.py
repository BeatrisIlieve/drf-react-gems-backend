from rest_framework import serializers

from rest_framework import serializers
from drf_react_gems_backend.user_credentials.models import UserCredentials
from drf_react_gems_backend.user_profile.models import UserProfile

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name"]
        
    def to_internal_value(self, data):
        instance = super().to_internal_value(data)
        instance["user"] = self.context["request"].user
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    pass

# class CreateUserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"

#     def validate_user_id(self, value):
#         try:
#             UserCredentials.objects.get(pk=value)
#         except UserCredentials.DoesNotExist:
#             raise serializers.ValidationError("The provided user ID does not exist.")
#         return value

#     def create(self, validated_data):
#         user_id = self.request.query_params.get("user_id", None)
        
#         user = UserProfile.objects.get(pk=user_id)

#         user_profile = UserProfile.objects.create(
#             # user=user,
#             first_name=first_name,
#             last_name=last_name,
#         )

#         return user_profile


# class CreateUserProfileSerializer(serializers.ModelSerializer):
#     # first_name = serializers.CharField(max_length=100)
#     # last_name = serializers.CharField(max_length=100)
#     # user_id = serializers.IntegerField()

#     class Meta:
#         model = UserProfile
#         fields = ["first_name", "last_name"]

#     def validate_user_id(self, value):
#         try:
#             UserCredentials.objects.get(pk=value)
#         except UserCredentials.DoesNotExist:
#             raise serializers.ValidationError("The provided user ID does not exist.")
#         return value

#     def create(self, validated_data):
#         user_id = self.request.query_params.get("user_id", None)
        
#         # user_id = validated_data.get("user_id")
#         first_name = validated_data.get("first_name")
#         last_name = validated_data.get("last_name")

#         # user = UserCredentials.objects.get(pk=user_id)
#         user = UserProfile.objects.get(pk=user_id)

#         user_profile = UserProfile.objects.create(
#             # user=user,
#             first_name=first_name,
#             last_name=last_name,
#         )

#         return user_profile
