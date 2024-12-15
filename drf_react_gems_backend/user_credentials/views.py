from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from rest_framework import generics as api_views
from rest_framework.authtoken import views as api_auth_views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from drf_react_gems_backend.user_credentials.serializers import (
    RegisterUserSerializer,
    UserEmailCheckSerializer,
)

from rest_framework.views import APIView

from drf_react_gems_backend.user_credentials.models import UserCredentials


class UserEmailCheckApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserEmailCheckSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        if UserCredentials.objects.filter(email=email).exists():
            return Response(
                {"email": "Email is already registered."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        validator = EmailValidator()

        try:
            validator(email)

        except ValidationError:
            return Response(
                {"error": "Please enter a valid email address."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            status=status.HTTP_200_OK,
        )


class RegisterUserApiView(api_views.CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginUserApiView(api_auth_views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.id,
            }
        )
