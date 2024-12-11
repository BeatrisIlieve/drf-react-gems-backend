from django.db import (
    models,
)
from django.db.models import (
    Min,
    Max,
    Sum,
    When,
    Case,
    Value,
    BooleanField,
)


class ProductManager(models.Manager):

    def represent_entity_into_products_list(self, category_pk, color_pk):
        return (
            self.filter(category__pk=category_pk, color__pk=color_pk)
            .select_related("category", "color")
            .prefetch_related("product_inventory")
            .annotate(
                min_price=Min("product_inventory__price"),
                max_price=Max("product_inventory__price"),
                total_quantity=Sum("product_inventory__quantity"),
                is_sold_out=Case(
                    When(total_quantity=0, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                ),
            )
        )

    def represent_entity_into_product_page(self, category_pk, color_pk):
        return (
            self.filter(category__pk=category_pk, color__pk=color_pk)
            .select_related("category", "color")
            .prefetch_related("product_inventory")
        )
