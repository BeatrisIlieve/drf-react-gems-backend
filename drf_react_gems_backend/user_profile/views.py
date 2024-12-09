from rest_framework import generics as api_views
from drf_react_gems_backend.user_profile.models import UserProfile
from drf_react_gems_backend.user_profile.serializers import (
    UserProfileCreateSerializer,
    UserProfileSerializer
)


class UserProfileApiView(api_views.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    create_serializer_class = UserProfileCreateSerializer
    list_serializer_class = UserProfileSerializer
    
    def get_serializer_class(self):
        if self.__is_get(self.request):
            return self.list_serializer_class
        
        return self.create_serializer_class
        
        
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if self.__is_get(self.request):
            queryset = queryset.filter(user=self.request.user)
        
        return queryset
    
    @staticmethod
    def __is_get(request):
        return request.method == "GET"