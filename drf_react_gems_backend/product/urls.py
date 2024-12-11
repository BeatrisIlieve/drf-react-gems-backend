from django.urls import path

from drf_react_gems_backend.product.views import (
    ProductListApiView,
    ProductDetailsApiView,
)

urlpatterns = (
    path(
        "list/",
        ProductListApiView.as_view(),
        name="product_list",
    ),
    path(
        "details/",
        ProductDetailsApiView.as_view(),
        name="product_details",
    ),
)
