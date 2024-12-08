from rest_framework import generics as api_views
from drf_react_gems_backend.user_profile.serializers import (
    CreateUserProfileSerializer,
)


class ApiCreateUserProfileView(api_views.CreateAPIView):
    serializer_class = CreateUserProfileSerializer