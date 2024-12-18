from django.urls import path


from drf_react_gems_backend.user_shipping_details.views import (
    UserShippingDetailsApiView,
    CountryListApiView,
    CityListApiView,
    # UserShippingDetailsUpdateApiView
)

urlpatterns = [
    path(
        "create/",
        UserShippingDetailsApiView.as_view(),
        name="user_shipping_details_api_view",
    ),
    path("countries/", CountryListApiView.as_view(), name="country-list"),
    path("cities/", CityListApiView.as_view(), name="city-list"),
    path("<int:pk>/", UserShippingDetailsApiView.as_view(), name="users"),
    # path("users-update/", UserShippingDetailsUpdateApiView.as_view(), name="users"),
]
