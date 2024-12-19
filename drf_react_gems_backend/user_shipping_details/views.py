from rest_framework import generics as api_views
from drf_react_gems_backend.user_shipping_details.models import UserShippingDetails
from drf_react_gems_backend.user_shipping_details.serializers import (
    # UserShippingDetailsCreateSerializer,
    UserShippingDetailsSerializer,
)

from cities_light.models import Country, City
from drf_react_gems_backend.user_shipping_details.serializers import CountrySerializer, CitySerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics


class CountryListApiView(api_views.ListAPIView):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer
    

class CityListApiView(api_views.ListAPIView):
    queryset = City.objects.all().order_by("name")
    serializer_class = CitySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()  # Retrieve the default queryset

        # Check if 'country' parameter is provided in the query parameters
        country_id = self.request.query_params.get('country', None)

        if country_id is not None:
            # Filter the queryset by country_id
            queryset = queryset.filter(country_id=country_id)
        
        return queryset
    


class UserShippingDetailsApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):

    queryset = UserShippingDetails.objects.all()
    serializer_class = UserShippingDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class UserShippingDetailsApiView(api_views.ListCreateAPIView):
#     queryset = UserShippingDetails.objects.all()
#     create_serializer_class = UserShippingDetailsCreateSerializer
#     list_serializer_class = UserShippingDetailsSerializer

#     def get_serializer_class(self):
#         if self.__is_get(self.request):
#             return self.list_serializer_class

#         return self.create_serializer_class

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         if self.__is_get(self.request):
#             queryset = queryset.filter(user=self.request.user)

#         return queryset

#     @staticmethod
#     def __is_get(request):
#         return request.method == "GET"

# class UserShippingDetailsUpdateApiView(api_views.RetrieveUpdateAPIView):
#     queryset = UserShippingDetails.objects.all()
#     serializer_class = UserShippingDetailsSerializer

#     def get_object(self):
#         obj, created = UserShippingDetails.objects.get_or_create(user=self.request.user)

#         if created:
#             obj.save()
#         return obj

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         queryset = queryset.filter(user=self.request.user)

#         return queryset


# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# class UserShippingDetailsApiView(APIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = UserShippingDetails.objects.all()
#     serializer_class = UserShippingDetailsSerializer


#     def get(self, request):
#         queryset = super().get_queryset()

#         queryset = queryset.filter(user=self.request.user)

#         return queryset

#         # shipping_details, created =UserShippingDetails.objects.get_or_create(user=request.user)
#         # serializer = UserShippingDetailsSerializer(shipping_details)
#         # return Response(serializer.data)

# def put(self, request):
#     """Update the user's shipping details."""
#     shipping_details, created = UserShippingDetails.objects.get_or_create(user=request.user)
#     serializer = UserShippingDetailsCreateSerializer(shipping_details, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Shipping details updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
