from rest_framework import generics as api_views
from drf_react_gems_backend.user_shipping_details.models import UserShippingDetails
from drf_react_gems_backend.user_shipping_details.serializers import (
    UserShippingDetailsCreateSerializer,
    UserShippingDetailsSerializer,
)


class UserShippingDetailsApiView(api_views.ListCreateAPIView):
    queryset = UserShippingDetails.objects.all()
    create_serializer_class = UserShippingDetailsCreateSerializer
    list_serializer_class = UserShippingDetailsSerializer

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
