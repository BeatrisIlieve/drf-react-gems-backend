from django.db import (
    models,
)

from django.db.models import (
    CharField,
    Min,
    Max,
    Sum,
)

from django.contrib.postgres.aggregates import (
    JSONBAgg,
)

from django.db.models.functions import (
    JSONObject,
    Cast,
)

from drf_react_gems_backend.utils.queries.get_full_category_title import (
    get_full_category_title,
)
from drf_react_gems_backend.utils.queries.get_full_color_title import (
    get_full_color_title,
)
from drf_react_gems_backend.utils.queries.get_stock_status_per_size import (
    get_stock_status_per_size,
)
from drf_react_gems_backend.utils.queries.get_stock_status_for_all_sizes import (
    get_stock_status_for_all_sizes,
)


class InventoryManager(models.Manager):

    def get_product_into_products_list(self, category_pk, color_pk):
        result = (
            self.filter(
                product__category_id=category_pk,
                product__color_id=color_pk,
            )
            .select_related("product", "product__category", "product__color")
            .values(
                "product_id",
                "product__category_id",
                "product__color_id",
                "product__first_image_url",
                "product__second_image_url",
                full_category_title=get_full_category_title(),
                full_color_title=get_full_color_title(),
            )
            .annotate(
                min_price=Min("price"),
                max_price=Max("price"),
                total_quantity=Sum("quantity"),
                is_sold_out=get_stock_status_for_all_sizes(),
            )
            .order_by("product_id")
        )

        return result

    def get_product_into_product_page(self, category_pk, color_pk):

        result = (
            self.filter(
                product__category_id=category_pk,
                product__color_id=color_pk,
            )
            .select_related("product", "product__category", "product__color")
            .values(
                "product_id",
                "product__category_id",
                "product__color_id",
                "product__first_image_url",
                "product__second_image_url",
                "product__description",
                full_category_title=get_full_category_title(),
                full_color_title=get_full_color_title(),
            )
            .annotate(
                inventory_details=JSONBAgg(
                    JSONObject(
                        inventory_id="id",
                        size="size",
                        price=Cast("price", output_field=CharField()),
                        is_sold_out=get_stock_status_per_size(),
                    ),
                    ordering=["size"],
                ),
                total_quantity=Sum("quantity"),
                is_sold_out=get_stock_status_for_all_sizes(),
            )
            .order_by("product_id")
        )

        return result
