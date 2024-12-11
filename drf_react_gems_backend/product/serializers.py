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
