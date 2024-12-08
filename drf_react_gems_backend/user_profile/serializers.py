from rest_framework import serializers
from django.db import IntegrityError
from rest_framework import serializers
from drf_react_gems_backend.user_credentials.models import UserCredentials
from drf_react_gems_backend.user_profile.models import UserProfile


# class RegisterUserSerializer(serializers.Serializer):

#     email = serializers.EmailField()
#     password = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data.pop("password")

#         return data

#     def validate_email(self, value):
#         if UserCredentials.objects.filter(email=value).exists():
#             raise serializers.ValidationError("This email is already in use.")
#         return value

#     def validate(self, attrs):
#         password = attrs.get("password", None)
#         # email = attrs.get("email", None)
#         try:
#             password_error = validate_password(password)
#         #     email_error = self.validate_email(email)
#         # except IntegrityError:
#         #     if email_error:
#         #         return {
#         #             "email": ["A user with this email already exists."],
#         #         }

#         #     if password_error:
#         #         return {"password": [password_error]}

#         finally:
#             return attrs

#     def create(self, validated_data):
#         email = validated_data["email"]
#         password = validated_data["password"]
#         first_name = validated_data["first_name"]
#         last_name = validated_data["last_name"]

#         user_credentials = UserCredentials.objects.create(
#             email=email,
#             password=make_password(password),
#         )

#         UserProfile.objects.create(
#             user=user_credentials,
#             first_name=first_name,
#             last_name=last_name,
#         )

#         return user_credentials


class CreateUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    
    class Meta:
        model = UserProfile
        fields = ["user_id", "first_name", "last_name"]


    def create(self, validated_data):
        """
        Create the user profile linked to the user_id.
        """
        user_id = validated_data.get("user_id")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")

        user = UserCredentials.objects.get(pk=user_id)  # Fetch user credentials

        # Create and return the user profile
        user_profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
        )

        return user_profile
