from enum import Enum

from abc import ABC, abstractmethod

from rest_framework import generics as api_views
from drf_react_gems_backend.inventory.models import Inventory
from drf_react_gems_backend.product.serializers import (
    ProductListSerializer,
    ProductDetailsSerializer,
)


# class ProductListApiView(api_views.ListAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = ProductListSerializer

#     def get_queryset(self):

#         queryset = super().get_queryset()

#         category_pk = self.request.query_params.get("category", None)
#         color_pk = self.request.query_params.get("color", None)

#         if category_pk and color_pk:
#             queryset = Inventory.objects.get_product_into_products_list(
#                 category_pk=category_pk, color_pk=color_pk
#             )

#         return queryset


# class ProductDetailsApiView(api_views.ListAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = ProductDetailsSerializer

#     def get_queryset(self):

#         queryset = super().get_queryset()

#         category_pk = self.request.query_params.get("category", None)
#         color_pk = self.request.query_params.get("color", None)

#         if category_pk and color_pk:
#             queryset = Inventory.objects.get_product_into_product_page(
#                 category_pk=category_pk, color_pk=color_pk
#             )

#         return queryset


class ProductStrategyType(Enum):
    PRODUCT_LIST = "product_list"
    PRODUCT_DETAILS = "product_details"


class BaseInventoryStrategy(ABC):
    @abstractmethod
    def get_filtered_queryset(self, category_pk, color_pk):
        pass


class ProductListStrategy(BaseInventoryStrategy):
    def get_filtered_queryset(self, category_pk, color_pk):
        return Inventory.objects.get_product_into_products_list(
            category_pk=category_pk, color_pk=color_pk
        )


class ProductDetailsStrategy(BaseInventoryStrategy):
    def get_filtered_queryset(self, category_pk, color_pk):
        return Inventory.objects.get_product_into_product_page(
            category_pk=category_pk, color_pk=color_pk
        )


class InventoryFilterContext:
    def __init__(self, strategy_type: ProductStrategyType):
        strategy_class = STRATEGY_MAPPER.get(strategy_type)
        self.strategy = strategy_class()

    def execute(self, category_pk, color_pk):
        return self.strategy.get_filtered_queryset(category_pk, color_pk)


class BaseProductApiView(api_views.ListAPIView):
    strategy_type = None  

    def get_queryset(self):
        queryset = super().get_queryset()

        category_pk = self.request.query_params.get("category")
        color_pk = self.request.query_params.get("color")

        if category_pk and color_pk:
            context = InventoryFilterContext(self.strategy_type)
            queryset = context.execute(category_pk, color_pk)

        return queryset


class ProductListApiView(BaseProductApiView):
    queryset = Inventory.objects.all()
    serializer_class = ProductListSerializer
    strategy_type = ProductStrategyType.PRODUCT_LIST


class ProductDetailsApiView(BaseProductApiView):
    queryset = Inventory.objects.all()
    serializer_class = ProductDetailsSerializer
    strategy_type = ProductStrategyType.PRODUCT_DETAILS


STRATEGY_MAPPER = {
    ProductStrategyType.PRODUCT_LIST: ProductListStrategy,
    ProductStrategyType.PRODUCT_DETAILS: ProductDetailsStrategy,
}
