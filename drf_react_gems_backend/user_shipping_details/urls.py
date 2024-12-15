from django.urls import path


from drf_react_gems_backend.user_shipping_details.views import (
    UserShippingDetailsApiView,
)

urlpatterns = [
    path(
        "create/",
        UserShippingDetailsApiView.as_view(),
        name="user_shipping_details_api_view",
    ),
]
