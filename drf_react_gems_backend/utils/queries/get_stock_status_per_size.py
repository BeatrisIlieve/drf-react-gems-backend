from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)


def get_stock_status_per_size():
    return Case(
        When(quantity=0, then=Value("Sold Out")),
        default=Value("In Stock"),
        output_field=CharField(),
    )
