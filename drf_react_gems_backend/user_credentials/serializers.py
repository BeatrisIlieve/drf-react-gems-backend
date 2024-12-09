from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_react_gems_backend.user_profile.models import UserProfile

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, "password")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password")
        
        # data["user_id"] = instance.id  
        
        return data

    def save(self, **kwargs):
        user = super().save(*kwargs)

        user.set_password(user.password)
        user.save()
        
        # UserProfile.objects.create(
        #     user=user,
        # )

        return user
    
    def validate(self, attrs):
        password = attrs.get("password", None)
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})

        try:
            validate_password(password)
        except Exception as e:
            raise serializers.ValidationError({"password": e})
        
        return attrs



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
