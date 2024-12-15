from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_react_gems_backend.user_profile.models import UserProfile
from drf_react_gems_backend.user_shipping_details.models import UserShippingDetails

UserModel = get_user_model()


class UserEmailCheckSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)  # Handle first_name for ShippingDetails

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, "password", "first_name")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password")  # Remove password from representation
        return data

    def create(self, validated_data):
        # Extract first_name for shipping details
        first_name = validated_data.pop('first_name', None)

        # Create the user with remaining data
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()

        # Create the shipping details record if first_name is provided
        if first_name:
            UserShippingDetails.objects.create(user=user, first_name=first_name)

        return user

    def validate(self, attrs):
        password = attrs.get("password", None)
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})

        try:
            validate_password(password)
        except Exception as e:
            raise serializers.ValidationError({"password": list(e)})

        return attrs



# class RegisterUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD, "password", "first_name")
#         fields = (UserModel.USERNAME_FIELD, "password")

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data.pop("password")

#         return data

#     def save(self, **kwargs):
#         user = super().save(*kwargs)

#         user.set_password(user.password)
#         user.save()

#         return user

#     def validate(self, attrs):
#         password = attrs.get("password", None)
#         if not password:
#             raise serializers.ValidationError({"password": "Password is required."})

#         try:
#             validate_password(password)
#         except Exception as e:
#             raise serializers.ValidationError({"password": list(e)})

#         return attrs


# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD, "password")

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data.pop("password")

#         data["user_id"] = instance.id
#         return data

#     def save(self, **kwargs):
#         user = super().save(*kwargs)

#         user.set_password(user.password)
#         user.save()

#         return user

#     def validate(self, attrs):
#         password = attrs.get("password", None)
#         try:
#             validate_password(password)
#         finally:
#             return attrs

#     # def validate(self, attrs):
#     #     password = attrs.get("password", None)
#     #     email = attrs.get("email", None)
#     #     try:
#     #         password_error = validate_password(password)
#     #         email_error = self.validate_email(email)
#     #     except IntegrityError:
#     #         if email_error:
#     #             return {
#     #                 "email": ["A user with this email already exists."],
#     #             }

#     #         if password_error:
#     #             return {"password": [password_error]}

#     #     finally:
#     #         return attrs
