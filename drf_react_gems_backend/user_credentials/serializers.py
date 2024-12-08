from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


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





class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, "password")
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password")
        
        data["user_id"] = instance.id  
        return data

    def save(self, **kwargs):
        user = super().save(*kwargs)

        user.set_password(user.password)
        user.save()

        return user

    def validate(self, attrs):
        password = attrs.get("password", None)
        try:
            validate_password(password)
        finally:
            return attrs
