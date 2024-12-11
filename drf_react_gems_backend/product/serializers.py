from rest_framework import serializers
from drf_react_gems_backend.inventory.models import Inventory


# class ProductListSerializer(serializers.ModelSerializer):
#     model = Inventory
#     fields = "__all__"


# # inventory_id = serializers.IntegerField()
# # size = serializers.CharField()
# # price = serializers.CharField()
# # stock_status = serializers.BooleanField()


# class ProductDetailsSerializer(serializers.ModelSerializer):
#     model = Inventory
#     fields = "__all__"


# # product_id = serializers.IntegerField()
# # product__category_id = serializers.IntegerField()
# # product__color_id = serializers.IntegerField()
# # product__first_image_url = serializers.URLField()
# # product__second_image_url = serializers.URLField()
# # product__description = serializers.CharField()
# # full_category_title = serializers.CharField()
# # full_color_title = serializers.CharField()
# # # inventory_details = InventoryDetailsSerializer(many=True)
# # total_quantity = serializers.IntegerField()
# # is_sold_out = serializers.BooleanField()


from rest_framework import serializers

class ProductListSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product__category_id = serializers.IntegerField()
    product__color_id = serializers.IntegerField()
    product__first_image_url = serializers.URLField()
    product__second_image_url = serializers.URLField()
    full_category_title = serializers.CharField()
    full_color_title = serializers.CharField()
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = serializers.IntegerField()
    is_sold_out = serializers.BooleanField()


class InventoryDetailSerializer(serializers.Serializer):
    inventory_id = serializers.IntegerField()
    size = serializers.CharField()
    price = serializers.CharField()
    is_sold_out = serializers.BooleanField()

class ProductDetailsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product__category_id = serializers.IntegerField()
    product__color_id = serializers.IntegerField()
    product__first_image_url = serializers.URLField()
    product__second_image_url = serializers.URLField()
    product__description = serializers.CharField()
    full_category_title = serializers.CharField()
    full_color_title = serializers.CharField()
    inventory_details = InventoryDetailSerializer(many=True)
    total_quantity = serializers.IntegerField()
    is_sold_out = serializers.BooleanField()
