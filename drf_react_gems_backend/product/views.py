from rest_framework import generics as api_views
from drf_react_gems_backend.inventory.models import Inventory
from drf_react_gems_backend.product.serializers import (
    ProductListSerializer,
    ProductDetailsSerializer,
)


class ProductListApiView(api_views.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        category_pk = self.request.query_params.get("category", None)
        color_pk = self.request.query_params.get("color", None)

        if category_pk and color_pk:
            queryset = Inventory.objects.get_product_into_products_list(
                category_pk=category_pk, color_pk=color_pk
            )

        return queryset


class ProductDetailsApiView(api_views.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = ProductDetailsSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        category_pk = self.request.query_params.get("category", None)
        color_pk = self.request.query_params.get("color", None)

        if category_pk and color_pk:
            queryset = Inventory.objects.get_product_into_product_page(
                category_pk=category_pk, color_pk=color_pk
            )

        return queryset
