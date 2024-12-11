from rest_framework import generics as api_views
from drf_react_gems_backend.product.models import Product
from drf_react_gems_backend.product.serializers import (
    ProductListSerializer,
    ProductDetailsSerializer,
)


class ProductListApiView(api_views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        category_id = self.request.query_params.get("category", None)
        color_id = self.request.query_params.get("color", None)

        if category_id and color_id:
            queryset = Product.objects.represent_entity_into_products_list(
                category_pk=category, color_pk=color
            )

        return queryset


class ProductDetailsApiView(api_views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer

    def get_queryset(self):

        queryset = super().get_queryset()

        category_id = self.request.query_params.get("category", None)
        color_id = self.request.query_params.get("color", None)

        if category_id and color_id:
            queryset = Product.objects.represent_entity_into_product_page(
                category_pk=category, color_pk=color
            )

        return queryset
