from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = serializers.IntegerField()
    is_sold_out = serializers.BooleanField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "color",
            "min_price",
            "max_price",
            "total_quantity",
            "is_sold_out",
        ]


class ProductDetailsSerializer(serializers.ModelSerializer):
    product_inventory = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "color",
            "product_inventory",
        ]
