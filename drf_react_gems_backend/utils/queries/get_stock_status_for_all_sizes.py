from django.db.models import (
    Case,
    When,
    Value,
    BooleanField,
)


def get_stock_status_for_all_sizes():
    return Case(
        When(total_quantity=0, then=Value("Sold Out")),
        default=Value("In Stock"),
        output_field=BooleanField(),
    )
