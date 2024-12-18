from django.urls import path


from drf_react_gems_backend.user_shipping_details.views import (
    UserShippingDetailsApiView,
    CountryListApiView,
    # UserShippingDetailsUpdateApiView
)

urlpatterns = [
    path(
        "create/",
        UserShippingDetailsApiView.as_view(),
        name="user_shipping_details_api_view",
    ),
    path("countries/", CountryListApiView.as_view(), name="country-list"),
    path("users/<int:pk>/", UserShippingDetailsApiView.as_view(), name="users"),
    # path("users-update/", UserShippingDetailsUpdateApiView.as_view(), name="users"),
]
